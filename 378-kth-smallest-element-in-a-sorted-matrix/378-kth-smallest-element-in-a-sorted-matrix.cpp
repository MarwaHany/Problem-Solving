class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        // 1D to 2D indexing
        // 1 2 3 4 5 6 
        // 1 2 3
        // 4 5 6
        // row = ? kth // matrix[0].size()
        // col = ? 3*row - 4
        int one_d_size = matrix.size() * matrix.back().size();
        vector<int> one_d;
        for(int i=0;i< matrix.size();i++){
            for(int j=0; j< matrix.back().size(); j++){
                one_d.push_back(matrix[i][j]);
            }
        }
        sort(one_d.begin(), one_d.end());
        for(int i=1;i<=one_d_size;i++){
         cout<<one_d[i-1]<<"/";   
        }
        cout<<endl;
        return one_d[k-1]; 
    }
};