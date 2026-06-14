class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int overWrite = 0;
        for (int i=0; i<(nums.size()); i++){
            if (nums[i] != 0){
                nums[overWrite] = nums[i];
                overWrite++;
            }
        }
        for (int i = overWrite; i<(nums.size()); i++){
            nums[i] = 0;
        }
    }
};