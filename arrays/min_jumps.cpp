//Walmart labs problem

int getMinJumps(string s){
    vector<int> ones;
 
    int jumps = 0, median = 0, ind = 0;
 
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '1')
            ones.push_back(i);
    }
 
    if (ones.size() == 0)
        return jumps;
 
    median = ones[ones.size() / 2];
    ind = median;
 
    for (int i = ind; i >= 0; i--) {
        if (s[i] == '1') {
            jumps += ind - i;
            ind--;
        }
    }
    ind = median;
 
    for (int i = ind; i < s.length(); i++) {
        if (s[i] == '1') {
            jumps += i - ind;
            ind++;
        }
    }
 
    return jumps;
}
