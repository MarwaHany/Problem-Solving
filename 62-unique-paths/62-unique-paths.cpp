using namespace std;
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> current_row(n);
        fill(current_row.begin(), current_row.end(),1);
        for(int i=0; i<m-1;i++){
            vector<int> temp_row(n);
            temp_row[n-1] = 1;
            for(int j=n-2; j>-1;j--){
                temp_row[j] = temp_row[j+1] + current_row[j];
            }
            current_row = temp_row;
        }
        return current_row.front();
    }
};