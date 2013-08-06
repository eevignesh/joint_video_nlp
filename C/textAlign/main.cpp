/*
	Created by Armand Joulin, 2013.
	Compute the alignement between two texts
	Partialy use code from Sten Hjelmqvist (through wikipedia)

	compile: g++ main.cpp -o align
*/

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm> 

using namespace std; 

int mydist(char a, char b){
	return (a==b)? 1 : 0;
}

int levenshtein_distance(string s, string t)
{
	// inspired by wikipedia (orginal by Hjelmqvist, Sten)

	// degenerate cases
	if (s == t) return 0;
	if (s.length() == 0) return t.length();
	if (t.length() == 0) return s.length();
	
	// create two work vectors of integer distances
	int v0[t.length() + 1];
	int v1[t.length() + 1];
	
	// initialize v0 (the previous row of distances)
	// this row is A[0][i]: edit distance for an empty s
	// the distance is just the number of characters to delete from t
	for (int i = 0; i < t.length() + 1; i++)
	    	v0[i] = i;
	
	for (int i = 0; i < s.length(); i++)
	{
	    // calculate v1 (current row distances) from the previous row v0
	
	    // first element of v1 is A[i+1][0]
	    //   edit distance is delete (i+1) chars from s to match empty t
	    v1[0] = i + 1;
	
	    // use formula to fill in the rest of the row
	    for (int j = 0; j < t.length(); j++)
	    {
	        int cost = (s[i] == t[j]) ? 0 : 1;
	        v1[j + 1] = min(min(v1[j] + 1, v0[j + 1] + 1), v0[j] + cost);
	    }
	
	    // copy v1 (current row) to v0 (previous row) for next iteration
	    for (int j = 0; j < t.length() + 1; j++)
	        v0[j] = v1[j];
	}
	
	return v1[t.length()];
}

float normalized_levenshtein_distance(string s, string t)
{
	return (max(s.length(), t.length()) != 0) ? ((float)levenshtein_distance(s, t)) / max(s.length(), t.length()) : 1;
}

int main(int argc, char* argv[]){

	// check for the right number of arguments
	if( argc < 3){
		cout << "Not enough input arguments (required: 2)" << endl;
		exit(EXIT_FAILURE);
	}

	// check if script file exists
	ifstream scriptfile;
	scriptfile.open (argv[1]);

    	if(!scriptfile)
    	{
		cout<< "Cannot open "<< argv[1] <<": Not such a file"<<endl;
		exit(EXIT_FAILURE);
    	} 

	// check if subtitle file exists
	ifstream subfile;
	subfile.open (argv[2]);
    	if(!subfile)
    	{
		cout<< "Cannot open "<< argv[2] <<": Not such a file"<<endl;
		exit(EXIT_FAILURE);
    	} 

	// copy script file to script
	vector<string> script;
	string buf;
        while(!scriptfile.eof()) 
        {
	        getline(scriptfile,buf); // Saves the line in buf.
		if(buf!="\n" && buf!="")
	        script.push_back(buf); // append to script.
        }
	scriptfile.close();	

	// copy subtitle file to sub
	vector<string> sub;
        while(!subfile.eof()) // To get you all the lines.
        {
	        getline(subfile,buf); // Saves the line in buf.
		if(buf!="\n" && buf!="")
	        sub.push_back(buf); // append to buf.
        }
	subfile.close();	


	// compute the distances (not required)
	int N2 = sub.size();
	int N1 = script.size();
	float dists[N2][N1];	
	for(int n2 = 0; n2 < N2; n2++)
		for(int n1 = n2; n1 < N1 - N2 + n2 + 1; n1++)
		{
			dists[n2][n1] = 1 - normalized_levenshtein_distance( sub[n2], script[n1]);
			// cout <<"diststance between: " << sub[n2] <<" / "<< script[n1] <<" : "<< dists[n2][n1]<<endl;
		}
	
	// forward pass: compute best cumulative scores
	float cumdists[N2][N1];	
	int ancestors[N2][N1];	
	for(int n2 = 0; n2 < N2; n2++)
		for(int n1 = n2; n1 < N1 - N2 + n2 + 1; n1++)
		{
			float maxcumdist = 0;
			int ancestor = -1;
			if( n2 > 0){
				for(int n11 = n2 - 1; n11 < n1; n11++ )
					if(maxcumdist < cumdists[n2-1][n11])
					{
						maxcumdist = cumdists[n2-1][n11];
						ancestor = n11;
					}
		}
			//cumdists[n2][n1] = normalized_levenshtein_distance(sub[n2], script[n1]) + maxcumdist;
			cumdists[n2][n1] = dists[n2][n1] + maxcumdist;
			ancestors[n2][n1] = ancestor;
		}	

	// backward pass: find best sub chain
	int n2 = N2-1, nb1 = -1;
	float maxcumdist = 0;
	for(int n1 = n2; n1 < N1 - N2 + n2 + 1; n1++)
		if(maxcumdist <= cumdists[n2][n1])
		{
			nb1 = n1;
			maxcumdist = cumdists[n2][n1];
		}
	// printing score
	cout << "best score: "<< maxcumdist << endl;

	// compute best pair of matches
	deque< pair<int,int> > subchain;
	while( nb1 != -1){
		if( dists[n2][nb1] != 0){
			subchain.push_front(make_pair(n2,nb1));
		}
		nb1 = ancestors[n2][nb1];
		n2 = n2 - 1;
	}

	// print results:
  	for (deque<pair<int,int> >::iterator it = subchain.begin(); it != subchain.end(); ++it)
    		cout << it->first << " "<< it->second << " ( \"" << sub[it->first] <<"\" matched to \""<< script[it->second] <<"\" )"<< endl;
	return 0;
}
