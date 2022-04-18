class Solution {
    public int maxProduct(int[] nums) {

        
        int res = Integer.MIN_VALUE;
        
        int currMax = 1;
        int currMin =1; //-1
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==0)
            {
                currMax =1;
                currMin =1;
            }
            int temp = currMax;    
            currMax = Math.max(Math.max(currMax*nums[i], currMin*nums[i]),nums[i]);
            currMin = Math.min(Math.min(temp*nums[i], currMin*nums[i]),nums[i]);
            
            
            res = Math.max(currMax, res);
            
        }
        
        return res;
        
        
    }
}