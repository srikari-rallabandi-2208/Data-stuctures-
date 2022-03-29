//AlgoExpert - non constructible change - Arrays

#include<vector>
#include<algorithm>
using namespace std;

int non_constructible_change(vector<int> coins){
	sort(coins.begin(), coins.end());
	int current_change_created = 0;
	for(int coin : coins){
		if(coin > current_change_created + 1)
			return current_change_created + 1;
		current_change_created += coin;
	}
	return current_change_created + 1;
}
