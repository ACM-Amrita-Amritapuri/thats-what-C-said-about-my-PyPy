
vector<int> SlidingWindowMaximum(int A[], int n, int K) {
        if (n * K == 0){
             return {};
        }
        vector<int> output(n - K + 1, 0);
        for (int i = 0; i < n - K + 1; i++) {
            int max = INT_MIN;
            for(int j = i; j < i + K; j++) 
                max = max(max, A[j]);
            output[i] = max;
        }
        return output;
    }