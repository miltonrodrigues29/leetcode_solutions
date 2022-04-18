class Solution {
    public int[] twoSum(int[] nums, int target) {
         
        int[] result = new int[2];
        HashMap<Integer,Integer> check = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            if(check.containsKey(target-nums[i]))
            {
              result[0] = i;
              result[1] = check.get(target-nums[i]);
                return result;
            }
            else
            {
                check.put(nums[i],i);
            }
        }
        return result;
        
    }
}