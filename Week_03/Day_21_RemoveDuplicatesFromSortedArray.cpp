class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int w=1;
        int r=1;
        while (r<nums.size()){
            if (nums[r]==nums[r-1]){
                r+=1;
            }else{
                nums[w]=nums[r];
                w+=1;
                r+=1;
            }
        }  
        return w;
    }
};