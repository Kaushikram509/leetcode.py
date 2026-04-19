class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        for(int i=0;i<n;i++){
            int current_element = nums[i];
            if(target <= current_element) {
                return i;
            }
        }
        return n;
    }
}
