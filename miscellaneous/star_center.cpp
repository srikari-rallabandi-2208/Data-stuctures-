//leetcode problem 1791 --- find center node of a star

#include<iostream>
#include<vector>

using namespace std;

int findCenter(vector<vector<int>>& e) {
    return e[0][0] == e[1][0] || e[0][0] == e[1][1] ? e[0][0] : e[0][1];
}

