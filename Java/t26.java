/**
 * 创建一个标志位，遍历数组，与标志位元素不相等时移动标志位并赋值
 * Author:lyc
*/

class Solution {
    public int removeDuplicates(int[] nums) {

        // 数组长度
        int numsOfLens = nums.length;

        // 标志位，默认为第一个元素
        int flag = 0;

        // 从数组第二个元素开始遍历
        for(int i=1;i<numsOfLens;i++){
            if(nums[i] != nums[flag]){
                flag += 1;
                nums[flag] = nums[i];
            }
        }

        return flag+1;

    }
}


public class t26 {

    public static void main(String[] args){

        int[] nums = {0,0,1,1,1,2,2,3,3,4};

        Solution result = new Solution();
        int res = result.removeDuplicates(nums);

        System.out.println(res);

    }
    
}