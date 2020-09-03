package app;

/*
leetcode 33
Author:lyc

题目：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
*/


public class t33 {
    public static void main(String[] args) {

        // 测试数据
        int nums[] = {4,5,6,7,0,1,2};
        int target = 3;

        Solution result = new Solution();
        int res = result.search(nums, target);
        System.out.println(res);

    }
}


class Solution {
    public int search(int[] nums, int target) {

        // 初始化左右两端索引
        int l = 0;
        int r = nums.length - 1;

        // 二分法
        while (l <= r){
            int mid = (l+r) / 2;
            // 返回条件
            if (target == nums[mid]){
                return mid;
            }

            if(nums[l] <= nums[mid]){
                // 二分法的基础上增加了判断条件
                if(nums[l] <= target && target <= nums[mid]){
                    r = mid;
                }else {
                    l = mid + 1;
                }
            }
            else {
                if(nums[mid] <= target && target <= nums[r]){
                    l = mid;
                }else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
}