#include <iostream>
#include<string>
#include<vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

int main()
{
	vector<string> words;
	vector<int> counts;

	//for(){
		//word in words vector?
			//++counts[?]
		//else
			//words.push_back(word);
			//counts.push_back(1);

	//}
	string word;
	while(cin >> word){
		vector<string>::size_type i;
		for (i = 0; i != words.size(); ++i){
			if(word == words[i])
				break;
		}

		if (i == words.size()) {// 해당하는 단어가 없다는 뜻
			words.push_back(word);// not found
			counts.push_back(1);
		}else{
			++counts[i];// found
		}
	}
	
	for (vector<string>::size_type i = 0; i != words.size(); ++i)
		cout << words[i] << " : " << counts[i] << endl;

	return 0;
}
