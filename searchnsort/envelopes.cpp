//LeetCode - problem 354

int maxEnvelopes(vector<pair<int, int& envelopes) {
        if (envelopes.empty()) return 0;
        sort(envelopes.begin(), envelopes.end());
        vector<int> dp(envelopes.size(), 1);
        for (int i = 0; i < envelopes.size(); ++i)
            for (int j = 0; j < i; ++j)
                if (envelopes[j].first < envelopes[i].first && envelopes[j].second < envelopes[i].second)
                    dp[i]  = max(dp[i] , dp[j] + 1);
        return *max_element(dp.begin(), dp.end());
    }
