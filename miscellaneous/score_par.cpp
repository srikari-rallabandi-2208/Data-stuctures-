//leetcode problem 856 - score of parentheses

int scoreOfParentheses(string s){
	int score = 0, mult = 1;
	for (int i = 0; i < s.;ength(); i++){
		if(s[i] == '('){
			if(s[i+1] == '('){
				mult *= 2;
			}
			else{
				score += mult;
				i++;
			}
		}
		else{
			mult = mult/2;
		}
	}
	return score;
}
