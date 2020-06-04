
/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

/**
 * 利用三个指针遍历交换
 * Author:lyc
*/
class Solution {
    public ListNode swapPairs(ListNode head) {

        /**传入链表为空或者只有一个元素时直接返回*/
        if(head == null){
            return null;
        }

        if(head.next == null){
            return head;
        }

        /**创建带有保护节点的链表*/
        ListNode result = new ListNode(0);
        result.next = head;

        /**创建三个移动指针*/
        ListNode first = result;
        ListNode mid = head;
        ListNode second = head.next;

        while(mid != null && second != null)
        {
            // 交换节点
            mid.next = second.next;
            second.next = mid;
            first.next = second;

            // 移动节点
            first = mid;
            mid = first.next;
            if(mid != null){
                second = mid.next;
            }
        }
        return result.next;

    }

    /**
     * 打印显示链表的元素，用于结果验证
    */
    public void showListNode(ListNode node){
        while(node != null){
            System.out.print(node.val+"\t");
            node = node.next;
        }
    }
}


public class t24 {

    public static void main(String[] args){

        // 创建测试链表
        ListNode node = new ListNode(1);
        node.next = new ListNode(2);
        node.next.next = new ListNode(3);
        node.next.next.next = new ListNode(4);

        // 验证结果
        Solution result = new Solution();
        ListNode res = result.swapPairs(node);

        result.showListNode(res);
    }
    
}

