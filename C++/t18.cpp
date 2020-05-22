#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 *  leetcode第18题
 *  在三数之和(t15)基础上加一层循环
 *  Author:lyc
*/

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {

        // 创建存放结果的vector
        vector<vector<int>> result {};

        if(nums.size() < 3){
            return result;
        };

        // 获取vector长度
        int numsOflens = nums.size();

        // vector排序
        sort(nums.begin(),nums.end());

        for(int a=0;a<numsOflens-3;a++)
        {
            if(a > 0 & nums[a] == nums[a-1])
            {
                continue;
            }
            for(int cur=a+1 ; cur < numsOflens-2 ; cur++)
            {
                // 当前元素和上一个元素相同时跳过
                if(cur > a+1 & nums[cur] == nums[cur-1])
                {
                    continue;
                };

                // 初始化 L R
                int L = cur + 1;
                int R = numsOflens - 1;

                while (L < R)
                {
                    // 计算四个数字加和
                    int sums = nums[a] + nums[cur] + nums[L] + nums[R];
                    // 开始与target作比较
                    if(sums == target)
                    {
                        vector<int> s {nums[a] , nums[cur] , nums[L] , nums[R]};
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
                    }
                    else if (sums > target)
                    {
                        R -= 1;
                    }
                    else
                    {
                        L += 1;
                    };
                };
            };
        };
        return result;
    };
};


int main()
{
    Solution model;

    //vector<int> x {1, 0, -1, 0, -2, 2};
    vector<int> x {0,0,0,0};
    int target = 0;

    vector<vector<int>> res = model.fourSum(x,target);

    // 遍历打印返回结果vector
    // for(int i=0;i<res.size();i++){
    //     for(int j=0;j<res[i].size();j++){
    //         cout << res[i][j] << "\t";
    //     };
    //     cout << endl;
    // }

    // C++ 11版本自动遍历vector方法
    for(auto i:res){
        for(auto j:i){
            cout << j << "\t";
        };
        cout << endl;
    }

    system("pause");
    return 0;
}



