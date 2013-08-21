#ifndef __UTILS_HPP__
#define __UTILS_HPP__

#include <vector>
#include <string>
#include <iostream>
#include <boost/algorithm/string/replace.hpp>

using namespace std;

static string removeHtmlTags(string html)
{
  //std::string html("<div style=\"width: 200px;\"><strong>Balance Sheets (USD $)<br></strong></div>");
  
  //std::string html(argv[1]);

  std::vector<std::string>    tags;
  std::vector<std::string>    text;

  for(;;)
  {
      std::string::size_type  startpos;

      startpos = html.find('<');
      if(startpos == std::string::npos)
      {
          // no tags left only text!
          text.push_back(html);
          break;
      }

      // handle the text before the tag    
      if(0 != startpos)
      {
          text.push_back(html.substr(0, startpos));
          html = html.substr(startpos, html.size() - startpos);
          startpos = 0;
      }

      //  skip all the text in the html tag
      std::string::size_type endpos;
      for(endpos = startpos;
          endpos < html.size() && html[endpos] != '>';
          ++endpos)
      {
          // since '>' can appear inside of an attribute string we need
          // to make sure we process it properly.
          if(html[endpos] == '"')
          {
              endpos++;
              while(endpos < html.size() && html[endpos] != '"')
              {
                  endpos++;
              }
          }
      }

      //  Handle text and end of html that has beginning of tag but not the end
      if(endpos == html.size())
      {
          html = html.substr(endpos, html.size() - endpos);
          break;
      }
      else
      {
          //  handle the entire tag
          endpos++;
          tags.push_back(html.substr(startpos, endpos - startpos));
          html = html.substr(endpos, html.size() - endpos);
      }
  }

  //std::cout << "tags:\n-----------------" << std::endl;

  // auto, iterators or range based for loop would probably be better but
  // this makes it a bit easier to read.    
  /*
  for(size_t i = 0; i < tags.size(); i++)
  {
      std::cout << tags[i] << std::endl;
  }

  std::cout << "\ntext:\n-----------------" << std::endl;*/

  string outString = "";
  for(size_t i = 0; i < text.size(); i++)
  {
      //std::cout << text[i] << std::endl;
      outString += string(text[i]);
  }
  boost::replace_all(outString, "\n", " ");
  return outString;
}


/*
  @brief: find and replace first occurrence of a substring in a string

  @parameter:
  s - stirng in which find and replace is carried out
  toReplace - substring to replace
  replaceWith - string to replace with

  @output:
  myreplce - string where toReplace is replaced with replaceWith

*/
static std::string myreplace(std::string &s,
                      std::string toReplace,
                      std::string replaceWith)
{
    return(s.replace(s.find(toReplace), toReplace.length(), replaceWith));
}

#endif
