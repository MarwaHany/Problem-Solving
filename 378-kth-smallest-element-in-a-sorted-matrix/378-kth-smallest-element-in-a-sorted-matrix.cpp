class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int one_d_size = matrix.size() * matrix.back().size();
        vector<int> one_d;
        for(int i=0;i< matrix.size();i++){
            for(int j=0; j< matrix.back().size(); j++){
                one_d.push_back(matrix[i][j]);
            }
        }
        sort(one_d.begin(), one_d.end());
        cout<<endl;
        return one_d[k-1]; 
    }
};