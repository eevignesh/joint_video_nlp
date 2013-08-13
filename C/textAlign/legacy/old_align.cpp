for(int i = 0; i < (finalWordAlignment.size() -2); i++)
  { 
    pair <int, pair <int, int> > sub_begin = finalWordAlignment[i];
    pair <int, pair <int, int> > sub_mid = finalWordAlignment[i+1];
    pair <int, pair <int, int> > sub_end= finalWordAlignment[i+2];

    // if both diaglogues belong to same block, you can skip
    int dialogueBeginBlock = script_parser._lineToBlockIndex[scriptWords._wordToSentenceIndex[sub_begin.second.second]];
    int dialogueMidBlock = script_parser._lineToBlockIndex[scriptWords._wordToSentenceIndex[sub_mid.second.first]];
    if(dialogueBeginBlock == dialogueMidBlock)
    {
      continue;
    }

    int srtCutBegin = sub_begin.first;
    int srtCutEnd = sub_end.first;

    int  scriptCutBegin = (sub_begin.second.second + 1);
    int scriptCutEnd = (sub_mid.second.first - 1);
  
    int blockBegin = script_parser._lineToBlockIndex[scriptWords._wordToSentenceIndex[scriptCutBegin]];
    int blockEnd = script_parser._lineToBlockIndex[scriptWords._wordToSentenceIndex[scriptCutEnd]];


    cout << scriptCutBegin << ":" << scriptCutEnd << "(" << script_parser._lines.size() << ")" << endl;
    if(scriptCutBegin <= scriptCutEnd && scriptCutEnd < (scriptWords._wordTokens.size()) 
        && matchScores[i] > SCORE_THRESH && matchScores[i+1] > SCORE_THRESH && matchScores[i+2] > SCORE_THRESH)
    {
      cout << srt_parser._timeStamps[srtCutBegin] << endl;
      cout << "Block " <<  blockBegin <<  ":" << blockEnd << endl;
      for (int j = scriptCutBegin; j <= scriptCutEnd; j++)
      {
        cout << scriptWords._wordTokens[j] << " ";
      }
      cout << endl;

    }
    else
    {
      cout << "ERRRROOOORRRR(" << srtCutBegin << "): " << scriptCutBegin << ", " << scriptCutEnd << endl;
    }

  }

