#include <iostream>
#include <boost/regex.hpp>
#include <string>
#include <stdlib.h>


using namespace std;
using namespace boost;

int main (int argc, char** argv)
{

  string S = "Ram#&39s mother is also Lakshmana#&39s mother!\n";
  boost::regex expression("(#&[0-9]+)");
  boost::match_results<std::string::const_iterator> results;
  
  if(boost::regex_match(S, results, expression))
  {
    for(int i = 0; i < results.size(); i++)
      cout << results[i] << endl;
  }

  return 0;
}
