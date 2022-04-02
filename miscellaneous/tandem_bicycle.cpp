//AlgoExpert - Tandem Bicycle - greedy algorithm

#include<vector>
#include<algorithm>

using namespace std;

void raip(vector<int> &array){
	int start = 0;
	int end = array.size() - 1;
	while (start < end){
		int temp = array[start];
		array[start] = array[end];
		array[end] = temp;
		start++;
		end--;
	}
}

int tandemBicycle(vector<int> rss, vector<int> bss, bool fastest){
	sort(rss.begin(), rss.end());
	sort(bss.begin(), bss.end());
	if(!fastest)
		raip(rss);
	int ts = 0;
	for (int i = 0; i < rss.size(); i++){
		int r1 = rss[i];
		int r2 = bss[bss.size() - i - 1];
		ts += max(r1, r2);
	}
	return ts;
}
