#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

/**
 *  leetcode第16题
 *  vector双端指针绝对值求解
 *  Author:lyc
*/


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {

        // 传入数组长度
        int numsOflens = nums.size();

        // 数组长度小于3，立即返回0
        if(numsOflens < 3){
            return 0;
        };

        // 排序
        sort(nums.begin(),nums.end());

        // 初始化一个比较大的结果值，会逐渐覆盖缩小
        int result = 10000;

        for(int cur=0; cur<numsOflens ; cur++){
            // 初始化两端指针
            int L = cur + 1;
            int R = numsOflens - 1;
            while (L < R)
            {
                int sum = nums[cur] + nums[L] + nums[R];
                if(sum == target){
                    return sum;
                };
                // 指针移动
                if(abs(target - sum) < abs(target - result)){
                    result = sum;
                }else if(sum > target){
                    R = R - 1;
                }else{
                    L = L + 1;
                };
            };
        };
    return result;
    };
};


int main()
{
    Solution model;

    vector<int> nums {-1,2,1,-4};
    int target = 1;

    int res = model.threeSumClosest(nums, target);

    cout << res <<endl;

    system("pause");
    return 0;
}




