//AlgoExpert - find largest 3 numbers

#include <vector>
#include<climits>
using namespace std;

void updateLargest(vector<int> &threeLargest, int num);
void shiftAndUpdate(vector<int> &largest, int num, int idx);

vector<int> findThreeLargestNumbers(vector<int> array){
	vector<int> threelargest{INT_MIN, INT_MIN, INT_MIN};
	for (num : array){
		updatelargest(threelargest, num);
	}
	return threelargest;
}

void updatelargest(vector<int> &threelargest,int num){
	if (num > threelargest[2]){
		shiftandupdate(threelargest, num, 2);
	}
	elif (num > threelargest[1]){
		shiftandupdate(threelargest, num, 1);
	}
	elif (num > threelargest[0]){
		shiftandupdate(threelargest, num, 0);
	}
}

void shiftandupdate(vector<int> &array,int num,int idx){
	for(int i = 0; i <= idx; i++){
		if (i == idx){
			array[i] = num;
		}
		else{
			array[i] = array[i + 1];
		}
	}
}
