class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        lefts_to_remove, rights_to_remove = 0, 0
        lefts, rights = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                lefts += 1
            elif s[i] == ')':
                if lefts > 0:
                    lefts -= 1
                else:
                    rights_to_remove += 1 
        lefts_to_remove = lefts 
        
        self.backtracking(0, 0, s, 0, '', ans, lefts_to_remove, rights_to_remove)
        if not ans:
            ans.append('')
        
        return ans
                    
    
    def backtracking(self, lefts, rights, s, ind, cur_str, ans, lefts_to_remove, rights_to_remove):
        if ind == len(s):
            if lefts == rights and lefts_to_remove==0 and rights_to_remove==0 and cur_str not in ans:
                ans.append(cur_str)
            return
        
        if s[ind] == '(':
            if lefts_to_remove > 0:
                self.backtracking(lefts, rights, s, ind+1, cur_str, ans, lefts_to_remove-1, rights_to_remove)
            self.backtracking(lefts+1, rights, s, ind+1, cur_str+'(', ans, lefts_to_remove, rights_to_remove)
            
        elif s[ind] == ')':
            if (lefts==0 or lefts>=rights) and rights_to_remove > 0:
                self.backtracking(lefts, rights, s, ind+1, cur_str, ans, lefts_to_remove, rights_to_remove-1)
            if lefts > rights:
                self.backtracking(lefts, rights+1, s, ind+1, cur_str+')', ans, lefts_to_remove, rights_to_remove)
            
        else:
            self.backtracking(lefts, rights, s, ind+1, cur_str+s[ind], ans, lefts_to_remove, rights_to_remove
