//LeetCode - problem 1825

class MKAverage {
public:
    multiset<int> left,mid,right;
    int m,k;
    long long s;
    vector<int> t;
    MKAverage(int m, int k) {
        this->m=m;
        this->k=k;
        s=0;
    }
    
    void addElement(int num) {
        t.push_back(num);
        if(t.size()<=m) {
            if(left.size()<k || num<*rbegin(left)) 
            {
                left.insert(num);
                if(left.size()>k) 
                {
                    mid.insert(*rbegin(left));
                    s+=*rbegin(left);
                    left.erase(prev(end(left)));
                    if(right.size()<k || *rbegin(mid)>*begin(right)) {
                        right.insert(*rbegin(mid));
                        s-=*rbegin(mid);
                        mid.erase(prev(end(mid)));
                        
                        if(right.size()>k) {
                            mid.insert(*begin(right));
                            s+=*begin(right);
                            right.erase(begin(right));
                        }
                    }
                    
                }
            } else {
                mid.insert(num);
                s+=num;
                if(right.size()<k||*rbegin(mid)>*begin(right)) {
                    right.insert(*rbegin(mid));
                    s-=*rbegin(mid);
                    mid.erase(prev(end(mid)));
                    if(right.size()>k) {
                        mid.insert(*begin(right));
                        s+=*begin(right);
                        right.erase(begin(right));
                    }
                }
            }
        }
        else {
                //delete val
                int val=t[t.size()-m-1];
                if(left.find(val)!=left.end()) {
                    left.erase(left.lower_bound(val));
                    left.insert(*begin(mid));
                    s-=*begin(mid);
                    mid.erase(begin(mid));
                } else if(mid.find(val)!=mid.end()) {
                    s-=val;
                    mid.erase(mid.lower_bound(val));
                } else {
                    right.erase(right.lower_bound(val));
                    right.insert(*rbegin(mid));
                    s-=*rbegin(mid);
                    mid.erase(prev(end(mid)));
                }
                //add num
                if(num<*rbegin(left)) {
                    left.insert(num);
                    mid.insert(*rbegin(left));
                    s+=*rbegin(left);
                    left.erase(prev(end(left)));
                } else {
                    mid.insert(num);
                    s+=num;
                    if(*rbegin(mid)>*begin(right)) {
                        right.insert(*rbegin(mid));
                        s-=*rbegin(mid);
                        mid.erase(prev(end(mid)));
                        mid.insert(*begin(right));
                        s+=*begin(right);
                        right.erase(begin(right));
                    }
                }
            }

    }
    
    int calculateMKAverage() {
    if(left.size()+right.size()+mid.size()<m) return -1;
    return s/(mid.size());

    }
};

