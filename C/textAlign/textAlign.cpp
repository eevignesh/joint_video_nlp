/*
	Created by Vignesh Ramanathan and Armand Joulin, 2013.
	Compute the alignement between two texts
	Partialy use code from Sten Hjelmqvist (through wikipedia)
*/

#ifndef __TEXT_ALIGN_CPP
#define __TEXT_ALIGN_CPP

#include "textAlign.hpp"

namespace alignment
{

  void SrtParser::parseFile(string srtFilename)
  {

    // first empty the time stamp and dialogue vectors
    _dialogues.clear();
    _timeStamps.clear();

    // check if subtitle file exists
    ifstream subfile;
    subfile.open (srtFilename.c_str());
    if(!subfile)
    {
      cout<< "Cannot open "<< srtFilename <<": Not such a file"<<endl;
      exit(EXIT_FAILURE);
    } 

    // to check what the current line is
    enum {
      LINE_ID,
      TIME_STAMP,
      DIALOGUE
    };

    int srtLineIdentifier = LINE_ID;
    int currentLineId = 0, prevLineId;
    string buf, dialogueBuffer;

    // parse the srt file
    vector<string> sub;
    while(!subfile.eof()) // To get you all the lines.
    {
      getline(subfile,buf); // Saves the line in buf.
      cout << buf << ":" << srtLineIdentifier << ":" << (int)(buf[0]) << endl;
      // Weirdly the break inbetween dialogues in a srt file is enforced by a charcter with ASCII value 13 !
      if (buf != "\n" && buf != "" && buf != " " && (int)(buf.c_str()[0]) != 13 && (int)(buf.c_str()[0]) != 0)
      {
        switch (srtLineIdentifier)
        {
          case LINE_ID: // to do if the line is a LINE_ID
            prevLineId = currentLineId;
            currentLineId = atoi(buf.c_str());

            // sanity check
            if (currentLineId != (prevLineId+1) && currentLineId != MAX_SRT_LINES)
            {
              cout << "The Srt file maybe corrupted at: " << prevLineId << endl;
              exit(EXIT_FAILURE);
            }
      
            srtLineIdentifier = TIME_STAMP;
            break;

          case TIME_STAMP: // to do if the line is a time stamp
            _timeStamps.push_back(buf);
            srtLineIdentifier = DIALOGUE;
            dialogueBuffer = "";
            break;

          case DIALOGUE: // to do if line is a dialogue
            std::transform(buf.begin(), buf.end(), buf.begin(), ::tolower);
            if (buf.c_str()[0] != '<')
              dialogueBuffer = dialogueBuffer + string(buf + string(" ")); // keep concatenating the dialogues
            break;      
        }
      }
      else
      {
        // in case of new line, set LINE_ID and push current dialogue into the vector
        cout << "blah" << currentLineId << ":" << (int)(buf == "") << endl;
        if (currentLineId>0)
        {
          srtLineIdentifier = LINE_ID;
          _dialogues.push_back(dialogueBuffer);

#ifdef DEBUG
          cout << "<" << currentLineId << "> : " <<  dialogueBuffer << endl;
#endif

        }
      }

      if(buf!="\n" && buf!="")
      {
        sub.push_back(buf); // append to buf.
      }
    }
   
    // last two lines in a srt are garbage, so pop them out ....
    if (!_dialogues.empty())
    {
      _dialogues.pop_back();
      _timeStamps.pop_back();
    }

    subfile.close();
  }


  /*******************************************************************************/

  _WordTokenizer::_WordTokenizer(vector <string> sentences)
  {
    int wordIndex = 0;
    //vector <string> wordsInSentence;

    for(int i = 0; i < sentences.size(); i++)
    {
      boost::tokenizer<> sentenceTokenizer(sentences[i]);

      //vector <string> wordsInSentence(sentenceTokenizer.begin(), sentenceTokenizer.end());
      _wordTokens.insert(_wordTokens.end(), sentenceTokenizer.begin(), sentenceTokenizer.end());
      _sentenceToWordIndex[i] = wordIndex;
      wordIndex = _wordTokens.size();

    }
  
  }

  /*******************************************************************************/

  _WordTokenizer::_WordTokenizer(string sentence)
  {
    int wordIndex = 0;
    //vector <string> wordsInSentence;

    boost::tokenizer<> sentenceTokenizer(sentence);
    _wordTokens.insert(_wordTokens.begin(), sentenceTokenizer.begin(), sentenceTokenizer.end());
    _sentenceToWordIndex[0] = wordIndex;      
  }


}
#endif
