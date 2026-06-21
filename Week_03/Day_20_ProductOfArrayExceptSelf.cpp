class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);
        int lprod = 1;
        int rprod = 1;
        for (int i= 0; i<n; i++){
            answer[i]*=lprod;
            lprod*= nums[i];

            answer[n-1-i]*=rprod;
            rprod*=nums[n-1-i];
        }
        return answer;
    }
};