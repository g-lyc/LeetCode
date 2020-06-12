class Solution {
    public int divide(int dividend, int divisor) {

        // 定义边界值
        int MIN_INT = Integer.MIN_VALUE;
        int MAX_INT = Integer.MAX_VALUE;

        if(dividend == 0) return 0;
        if(divisor == 1) return dividend;
        if(divisor == -1){
            if(dividend>MIN_INT) return -dividend;
            return MAX_INT;
        }

        // 取绝对值，方便运算
        long f = Math.abs((long)dividend);
        long r = Math.abs(divisor);

        // 初始化结果值
        long count = 0;

        while(f >= r)
        {
            int flag = 0;
            long tmp = r;

            // 迭代被除数减去除数的位运算
            while(f >= tmp)
            {
                f -= tmp;
                count += 1 << flag;
                tmp <<= 1;
                flag += 1;
            }
        }

        // 判断异号及边界
        if(dividend < 0 && divisor > 0){
            count = -count;
            if(count < MIN_INT){
                return MIN_INT;
            }
        }

        if(dividend > 0 && divisor < 0){
            count = -count;
            if(count < MIN_INT){
                return MIN_INT;
            }
        }

        if(count > MAX_INT){
            return MAX_INT;
        }

        return (int)count;

    }
}

public class t29 {

    public static void main(String[] args){

        Solution result = new Solution();

        int dividend = -2147483648;
        int divisor = 2;

        int res = result.divide(dividend, divisor);

        System.out.println(res);

    }
    
}