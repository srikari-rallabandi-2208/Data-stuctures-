//LeetCode - problem 13

int romanToInt(string s) {
        unordered_map<char,int>m;
        int ans=0;
        m['I']=1;
        m['V']=5;
        m['X']=10;
        m['L']=50;
        m['C']=100;
        m['D']=500;
        m['M']=1000;
        int i=0;
            while(s[i]!='\0'){
                if(m[s[i]]<m[s[i+1]]){
                    ans=ans+m[s[i+1]]-m[s[i]];
                    i=i+2;
                }
                else{
                    ans=ans+m[s[i]];
                    i++;
                    
                }     
            }
                return ans;     
            
        
    }
