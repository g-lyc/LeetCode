package app;

/*
leetcode 34
Author：lyc

题目：
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
*/


public class t34 {
    public static void main(String[] args) {
        int nums[] = {5,7,7,8,8,10};
        int target = 8;

        Solution result = new Solution();
        int res[] = result.searchRange(nums, target);

        for (int i=0;i<res.length;i++){
            System.out.println(res[i]);
        }
    }
}

class Solution {
    public int[] searchRange(int[] nums, int target) {

        int res[] = {-1,-1};

        // for循环执行两边，第一次找左边界索引，第二次找右边界索引
        for (int i=1;i<=2;i++){

            // 每次都需要初始化左右指针
            int l = 0;
            int r = nums.length - 1;

            while (l <= r){
                // 正常二分法判断左右指针对应元素和target比较
                int mid = (l+r) / 2;
                if(nums[mid] > target){
                    r = mid - 1;
                }else if (nums[mid] < target){
                    l = mid + 1;
                }else {
                    // 正常二分法此处应该返回，针对找边界问题还需要判断
                    // 这是判断是第一次还是第二次
                    // 根据判断结果决定移动左指针还是右指针
                    if(i == 1){
                        res[0] = mid;
                        r = mid - 1;
                    }else {
                        res[1] = mid;
                        l = mid + 1;
                    }
                }
            }
        }

        return res;

    }
}
