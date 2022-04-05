//LeetCode - problem 1700 - Number of Students Unable to Eat Lunch

int countStudents(vector<int>& A, vector<int>& B) {
        int count[] = {0, 0}, n = A.size(), k;
        for (int a : A)
            count[a]++;
        for (k = 0; k < n && count[B[k]] > 0; ++k)
            count[B[k]]--;
        return n - k;
    }

