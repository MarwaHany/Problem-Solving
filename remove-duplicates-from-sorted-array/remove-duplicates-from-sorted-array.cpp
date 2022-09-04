class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        map<int, int> mymap;
        vector<int> temp;
        int count = 0;
        for(int i=0; i<nums.size();i++){
            if (mymap.count(nums[i]) > 0){
                continue;
            }
            else{
                mymap[nums[i]] = 1;
                temp.push_back(nums[i]);
                count++;
            }
        }
        nums = temp;
        return count;
    }
};