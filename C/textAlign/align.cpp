/*
	Created by Vignesh Ramanathan and Armand Joulin, 2013.
  Main function to carry out text alignment	
*/

#include "textAlign.hpp"
#include "tvParser.hpp"
#include <boost/algorithm/string.hpp>

using namespace alignment;

string time2d(int timeNum, char tempTime[])
{
  sprintf(tempTime, "%02d", timeNum);
  string timeString(tempTime);
  return timeString;
}

int main(int argc, char* argv[])
{

	// check for the right number of arguments
  if( argc < 4){
  	cout << "Not enough input arguments (required: 2)" << endl;
  	exit(EXIT_FAILURE);
  }

  // the output file to store the time ends
  // and the descriptions
  string outFilename(argv[3]);
 
  // parse the srt file
  SrtParser srt_parser;
  srt_parser.parseFile(argv[2]);

  HocrScriptParser script_parser;
  script_parser.parseFile(argv[1]);

  // tokenize script to word tokens
  WordTokenizer scriptWords(script_parser._dialogues, 
      script_parser._lineToBlockIndex, script_parser._dialogueToLineIndex);

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
  deque <float> matchScores;


  /**************************************
   * OPTION 1 - do word to word alignment
   * *************************************
   *
     WordTokenizer subWords(srt_parser._dialogues); 
     getTimeSynchDistance(subWords._wordTokens, scriptWords._wordTokens, normalized_levenshtein_distance, finalWordAlignment, true);  
  */


  /* *******************************************
   * OPTION 2 - slower but more accurate alignment, whre substring alignment is done throug DP as well
   * ********************************************
   */ 
    getTimeSynchDistance(subWordTokens, scriptWords._wordTokens, timeSynchDistanceWithAlignment, finalWordAlignment, matchScores, true);
  
  
  // OPTION 3 - faster but slightly less accurate, uses a greedy scheme for string matchin when comparing
  // subtitle string to a sub-segment of the script
  //getTimeSynchDistance(subWordTokens, scriptWords._wordTokens, greedyTimeSynchDist, finalWordAlignment, true);
  
  
  /* 
   * 
   * UNCOMMENT to print the alignment from the script to get only action segments without dialogue
   *
   */
   // get the time-synched scripts
#ifdef DEBUG
  cout << "Starting complete line distance measurement ... " << endl;
#endif
  
  // First, pool the time-stamps for different dialogue blocks
  for(int i = 0; i < (finalWordAlignment.size()) ; i++)
  {

    if(matchScores[i] < SCORE_THRESH)
    {
      continue;
    }

    pair <int, pair <int, int> > subId = finalWordAlignment[i];
    pair <int,int> srtTime = parseTime(srt_parser._timeStamps[subId.first]);

    /*
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    cout << "Matching happens at : " << srt_parser._dialogues[subId.first] << " MATCHES TO WORDS " << scriptWords._wordTokens[subId.second.first] << "  ---- TO ---- " << scriptWords._wordTokens[subId.second.second] << endl;
    cout << "\" " << script_parser._dialogues[scriptWords._wordToSentenceIndex[subId.second.first]] << " \" " << " ... to ... " << " \" ";
    cout << script_parser._dialogues[scriptWords._wordToSentenceIndex[subId.second.second]] << " \" " << endl;
    */

    int dialogueBlockId_beg = script_parser._dialogueToLineIndex[scriptWords._wordToSentenceIndex[subId.second.first]];
    dialogueBlockId_beg = script_parser._lineToBlockIndex[dialogueBlockId_beg];
    
    int dialogueBlockId_end = script_parser._dialogueToLineIndex[scriptWords._wordToSentenceIndex[subId.second.second]];
    dialogueBlockId_end = script_parser._lineToBlockIndex[dialogueBlockId_end];

    if(dialogueBlockId_beg <= dialogueBlockId_end)
    {
      //cout << "dialogue Id: " << dialogueBlockId_beg << endl;
      // First do it for the block where the dialogue begins
      pair<int,int> ts = script_parser._timeStamps[dialogueBlockId_beg];
      if (ts.first == -1 || ts.first > srtTime.first )
      {
        ts.first = srtTime.first;
      }

      if (ts.second == -1 || ts.second < srtTime.second )
      {
        ts.second = srtTime.second;
      }
      script_parser._timeStamps[dialogueBlockId_beg] = ts;

      // Next do it for the block where the dialogue ends
      ts = script_parser._timeStamps[dialogueBlockId_end];
      if (ts.first == -1 || ts.first > srtTime.first )
      {
        ts.first = srtTime.first;
      }

      if (ts.second == -1 || ts.second < srtTime.second )
      {
        ts.second = srtTime.second;
      }
      script_parser._timeStamps[dialogueBlockId_end] = ts;

    }
    else
    {
      cout << "Some time alignment error in assigning dialogue ids !" << endl;
    }  
  }


  ofstream outFile(outFilename.c_str());
  char tempTime[4];

  // Display the dialogues aligned in the script with time-stamp
  for(int i = 0; i < (script_parser._dialogueBlockIds.size() - 2); i++)
  {
    int blockId_1 = script_parser._dialogueBlockIds[i];
    int blockId_2 = script_parser._dialogueBlockIds[i+1];
    int blockId_3 = script_parser._dialogueBlockIds[i+2];

    pair <int, int> descrTimeStamp = assertTimeStamps(script_parser._timeStamps[blockId_1], script_parser._timeStamps[blockId_2], script_parser._timeStamps[blockId_3]);

    if (descrTimeStamp.first == -1 || descrTimeStamp.second == -1)
    {
      continue;
    }
    // cout << "B1 = " << blockId_1 << " , B2 = " << blockId_2 << " ============================ " << endl;
    vector <string> description;
    for(int j = blockId_1; j <= blockId_2; j++)
    {
      if(script_parser._blocks[j]._blockId == DESCRIPTION)
      {
        ScriptBlock dBlock= script_parser._blocks[j];
        for(int k = 0; k < dBlock._scriptLines.size(); k++)
        {
          description.push_back(script_parser._hocrSentences[dBlock._scriptLines[k]].line);
        }
      }
    }

    if (description.size() > 0)
    {
      cout << "time: " << descrTimeStamp.first << " --> " << descrTimeStamp.second << endl;

      descrTimeStamp.first = descrTimeStamp.first - 20;
      descrTimeStamp.first = descrTimeStamp.first>0? descrTimeStamp.first: 0;

      int hh_beg = (descrTimeStamp.first)/3600;
      int mm_beg = (descrTimeStamp.first%3600)/60;
      int ss_beg = ((descrTimeStamp.first%3600)%60);

      descrTimeStamp.second = descrTimeStamp.second + 20 - descrTimeStamp.first;

      int hh_end = (descrTimeStamp.second)/3600;
      int mm_end = (descrTimeStamp.second % 3600) / 60;
      int ss_end = ((descrTimeStamp.second % 3600) % 60);
      
      outFile << time2d(hh_beg, tempTime) << ":" << time2d(mm_beg, tempTime) << ":" << time2d(ss_beg, tempTime) << endl;
      outFile << time2d(hh_end, tempTime) << ":" << time2d(mm_end, tempTime) << ":" << time2d(ss_end, tempTime) << endl;

      for(int j = 0; j < description.size(); j++)
      {
        string sDescription(description[j]);
        boost::replace_all(sDescription, "\n", " ");
        
        cout << sDescription << " ";
        outFile << sDescription << " ";
      }

      outFile << endl << endl;
      cout << endl;

    }
    
    /*  
    cout << "time: " << script_parser._timeStamps[blockId].first << " --> " << script_parser._timeStamps[blockId].second << endl;
    for(int j = 0; j < script_parser._blocks[blockId]._scriptLines.size(); j++)
    {
      cout << script_parser._hocrSentences[script_parser._blocks[blockId]._scriptLines[j]].line  << endl;
    }*/
  
  }

  outFile.close();
  
  return 0;

}

