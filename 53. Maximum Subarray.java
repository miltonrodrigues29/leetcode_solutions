class Solution {
    

    public int maxSubArray(int[] nums) {
       //[-1,2,4]
       int maxSum = nums[0]; //-1 -> -1 -> 2 -> 4  // loop ends, return 4.
       int curSum =0; //0 -> -1 -> 2 -> 4
       for(int i=0;i<nums.length;i++)
       {
           if(curSum<0)
           {
               curSum =0;
           }
           
         curSum = curSum + nums[i];
         maxSum = Math.max(maxSum,curSum);
         
       }
        
        return maxSum;
       
    }
}