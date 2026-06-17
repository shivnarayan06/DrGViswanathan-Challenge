class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int check = 0;
        for (int i = 0; i<nums.size(); i++){
            check^=nums[i];
        }
        return check;
    }
};
