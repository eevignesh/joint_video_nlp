/*
	Created by Vignesh Ramanathan and Armand Joulin, 2013.
  Main function to carry out text alignment	
*/

#include "textAlign.hpp"

using namespace alignment;

int main(int argc, char* argv[])
{

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

  // copy script file to script
  vector<string> script;
  string buf; string old_buf = "";
  while(!scriptfile.eof()) 
  {
	getline(scriptfile,buf); // Saves the line in buf.
	if(buf!="\n" && buf!="")
    	{
      		std::transform(buf.begin(), buf.end(), buf.begin(), ::tolower);
	    	script.push_back(buf); // append to script.
      		old_buf = buf + string(" ");
    	}
  }
  scriptfile.close();	

  // parse the srt file
  SrtParser srt_parser;
  srt_parser.parseFile(argv[2]);

  // tokenize script to word tokens
  WordTokenizer scriptWords(script);

  // Now tokenize each dialogue, and insert the words to a vector of words
  vector <vector <string> > subWordTokens;
  for (int i = 0; i < srt_parser._dialogues.size(); i++)
  {
    WordTokenizer dialogueWords(srt_parser._dialogues[i]);
    subWordTokens.push_back(dialogueWords._wordTokens);
  }
  
  // the double ended queue to store the matching index pair
  // <subtitle index, <matching begining in script, matching end in script> >
  deque < pair <int, pair<int, int> > > finalWordAlignment;

  /**************************************
   * OPTION 1 - do word to word alignment
   * *************************************
   *
     WordTokenizer subWords(srt_parser._dialogues); 
     getTimeSynchDistance(subWords._wordTokens, scriptWords._wordTokens, normalized_levenshtein_distance, finalWordAlignment, true);  
  */


  /* *******************************************
   * OPTION 2 - slower but more accurate alignment, whre substring alignment are done throug DP as well
   * ********************************************
   * 
    getTimeSynchDistance(subWordTokens, scriptWords._wordTokens, timeSynchDistanceWithAlignment, finalWordAlignment, true);
  */
  
  // OPTION 3 - faster but slightly less accurate, uses a greedy scheme for string matchin when comparing
  // subtitle string to a sub-segment of the script
  getTimeSynchDistance(subWordTokens, scriptWords._wordTokens, greedyTimeSynchDist, finalWordAlignment, true);
  
  
  /* 
   * 
   * UNCOMMENT to print the alignment from the script to get only action segments without dialogue
   *
   *
   // get the time-synched scripts
#ifdef DEBUG
  cout << "Starting complete line distance measurement ... " << endl;
#endif
  deque < pair<int, int> > finalAlignment;
  getTimeSynchDistance(srt_parser._dialogues, script, timeSynchDistance, finalAlignment, true);

  for(int i = 0; i < (finalAlignment.size() -2); i++)
  { 
    pair <int, int> it = finalAlignment[i];
    pair <int, int> end_align= finalAlignment[i+2];

    int srtMatch = it.first;
    int scriptMatch = it.second;
    
    int  scriptCutBegin = scriptMatch + 1;
    int scriptCutEnd = (end_align.second - 2);

    if(scriptCutBegin <= scriptCutEnd && scriptCutEnd < (script.size()) )
    {
      cout << " =============================================== " << endl;
      cout << srtMatch << " "<< scriptMatch << " ( \"" << srt_parser._dialogues[srtMatch] <<"\" matched to \""<< script[scriptMatch] <<"\" )"<< endl;
      cout << " =============================================== " << endl;
      cout << srt_parser._timeStamps[srtMatch] << endl;
      for(int j = scriptCutBegin; j <= scriptCutEnd; j++)
      {
        cout << script[j] << endl;
      }
      cout << endl;
    
    }
    else
    {
      cout << "ERRRROOOORRRR(" << srtMatch << "): " << scriptCutBegin << ", " << scriptCutEnd << endl;
    }

  }
*/
  return 0;

}

