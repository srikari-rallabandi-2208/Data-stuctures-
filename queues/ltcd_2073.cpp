//LeetCode - problem 2073

int timeRequiredToBuy(vector<int>& tickets, int k) {
    int cnt = 0 , i = 0 , n = tickets.size();
    while(1){
        if(tickets[i % n]) 
            cnt++ , tickets[i % n]--;
        i++;
        if(!tickets[k])
            return cnt;
    }
}
