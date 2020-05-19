#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 *  leetcode第15题
 *  vector排序+双端指针搜索
 *  Author:lyc
*/


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums){

        // 创建存放结果的vector
        vector<vector<int>> result {};

        if(nums.size() < 3){
            return result;
        };

        // 获取vector长度
        int numsOflens = nums.size();

        // vector排序
        sort(nums.begin(),nums.end());

        for(int cur=0 ; cur < numsOflens ; cur++){

            // 当前元素大于0时直接返回
            if(nums[cur] > 0){
                return result;
            };

            // 当前元素和上一个元素相同时跳过
            if(cur > 0 & nums[cur] == nums[cur-1]){
                continue;
            };

            // 初始化 L R
            int L = cur + 1;
            int R = numsOflens - 1;

            while (L < R){
                if(nums[cur] + nums[L] + nums[R] == 0){
                    vector<int> s {nums[cur] , nums[L] , nums[R]};
                    result.push_back(s);
                    // 指针移动
                    while (L < R & nums[L] == nums[L + 1]){
                        L += 1;
                    };

                    while (L < R & nums[R] == nums[R - 1]){
                        R -= 1;
                    };

                    L += 1;
                    R -= 1;
                }else if (nums[cur] + nums[L] + nums[R] > 0){
                    R -= 1;
                }else{
                    L += 1;
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution model;

    vector<int> x {-1, 0, 1, 2, -1, -4};

    vector<vector<int>> res = model.threeSum(x);

    // 遍历打印返回结果vector
    for(int i=0;i<res.size();i++){
        for(int j=0;j<res[i].size();j++){
            cout << res[i][j] << "\t";
        };
        cout << endl;
    }

    system("pause");
    return 0;
}



