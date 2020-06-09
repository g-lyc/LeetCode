/**
 * 创建一个标志位，遍历数组，与输入的val元素不相等时移动标志位并赋值
 * Author:lyc
*/

class Solution {
    public int removeElement(int[] nums, int val) {

        // 数组长度
        int numsOfLens = nums.length;

        // 标志位，默认为第一个元素
        int flag = 0;

        // 遍历数组，遇到与标志位元素不相等的情况，将当前元素赋值给标志位并且后移一位
        for(int i=0;i<numsOfLens;i++){
            if(nums[i] != val){
                nums[flag] = nums[i];
                flag += 1;
            }
        }

        return flag;

    }
}


public class t27 {

    public static void main(String[] args){

        int[] nums = {3,2,2,3};

        int val = 3;

        Solution result = new Solution();
        int res = result.removeElement(nums, val);

        System.out.println(res);

    }
    
}