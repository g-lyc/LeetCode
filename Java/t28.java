
/**
 * Author:lyc
*/
class Solution {
    public int strStr(String haystack, String needle) {

        // 如果输入匹配字符为空直接返回
        if(needle.length() == 0){
            return 0;
        }

        // 设置结果baiozhi符
        int result = -1;

        // 当匹配字符长度大于查询的字符时直接返回
        if(haystack.length() < needle.length()){
            return result;
        }

        // 遍历查询的字符串，遍历长度需要减去匹配的字符串长度再加1
        for(int i=0;i<haystack.length()-needle.length()+1;i++){
            // 首个字符相同时开始遍历匹配字符串
            if(haystack.charAt(i) == needle.charAt(0)){
                boolean flag = true;
                for(int j=0;j<needle.length();j++){
                    // 一旦出现不相同的字符更改flag状态并退出本次循环，退出是关键
                    if(needle.charAt(j) != haystack.charAt(i+j)){
                        flag = false;
                        break;
                    }
                }

                if(flag){
                    return i;
                }
            }
        }
        return result;
    }
}


public class t28 {

    public static void main(String[] args){

        String haystack = "a";
        String needle = "a";

        Solution result = new Solution();

        int res = result.strStr(haystack, needle);

        System.out.println(res);
    }
    
}