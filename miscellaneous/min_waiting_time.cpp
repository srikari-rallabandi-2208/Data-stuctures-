//AlgoExpert - minimum waiting time - Greedy algorithms

#include<vector>
#include<algorithm>

using namespace std;

int min_waiting_time(vector<int> queries){
	sort(queries.begin(), queries.end());
	int total_waiting_time = 0;
	for(int i = 0; i < queries.size(); i++){
		int duration = queries[i];
		int queries_left = queries.size() - (i + 1);
		total_waiting_time += duration + queries_left;
	}
	return total_waiting_time
}
