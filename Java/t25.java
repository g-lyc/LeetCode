
/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

/**
 * 利用双指针遍历，对k长度的子链表反转拼接
 * Author:lyc
*/
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {

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

        /**创建两个移动指针*/
        ListNode pre = result;
        ListNode end = result;

        // 让end指针先跑k步，不够k步时直接返回result链表
        while(end != null){
            for(int i=0;i<k;i++){
                end = end.next;
                if(end == null){
                    return result.next;
                }
            }

            // 创建两个节点切断链表
            ListNode startNode = pre.next;
            ListNode endNode = end.next;
            end.next = null;

            // 子链表反转
            pre.next = reverse(startNode);

            // 子链表和原来剩余的链表拼接
            startNode.next = endNode;

            // 重置pre和end指针进行下一轮迭代
            pre = startNode;
            end = pre;
        }
        return result.next;
    }

    /**
     * 子链表反转函数
    */
    public ListNode reverse(ListNode head){

        ListNode pre = null;
        ListNode pnext = null;
        while(head != null){
            // 保存当前节点之后的链表
            pnext = head.next;
            // 当前节点下一个元素设置为pre
            head.next = pre;
            // pre更新为当前元素
            pre = head;
            // head更新，往后走一步，迭代
            head = pnext;
        }
        return pre;
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


public class t25 {

    public static void main(String[] args){

        // 创建测试链表
        ListNode node = new ListNode(1);
        node.next = new ListNode(2);
        node.next.next = new ListNode(3);
        node.next.next.next = new ListNode(4);
        node.next.next.next.next = new ListNode(5);

        int k=2;

        // 验证结果
        Solution result = new Solution();
        ListNode res = result.reverseKGroup(node, k);

        result.showListNode(res);
    }
    
}

