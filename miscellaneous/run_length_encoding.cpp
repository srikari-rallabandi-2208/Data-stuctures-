//AlgoExpert - run-length encoding - strings

#include<vector>
using namespace std;

string rle(string str){
	vector<char> esc;
	int crl = 1;
	for(int i = 1; i < str.size(); i++){
		char cc = str[i];
		char pc = str[i - 1];
		if (cc != pc || crl == 9){
			esc.push_back(to_string(crl)[0]);
			esc.push_back(pc);
			crl = 0;
		}
		crl ++;
	}
	esc.push_back(to_string(crl)[0]);
	esc.push_back(str[str.size() - 1]);
	string es(esc.begin(),esc.end());
	return es;
}
