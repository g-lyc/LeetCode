import java.util.ArrayList;
import java.util.Collections; 

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

/**
 * 将所有链表元素提取出来放在数组排序之后再逐个添加至新链表
*/
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        // 输入链表数组长度为1时直接返回该链表
        if(lists.length == 1){
            return lists[0];
        }

        // 取出所有元素放在数组中
        ArrayList<Integer> node_list = new ArrayList<Integer>();
        for(int i=0;i<lists.length;i++){
            while(lists[i] != null){
                node_list.add(lists[i].val);
                lists[i] = lists[i].next;
            }
        }
        
        // 排序
        Collections.sort(node_list);

        ListNode new_node = new ListNode(0);
        ListNode resut;
        resut = new_node;

        // 将排序后的数组元素逐个添加至新链表
        for(Integer i:node_list){
            new_node.next = new ListNode(i);
            new_node = new_node.next;
        }
        return resut.next;
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


public class t23 {

    public static void main(String[] args){

        // 创建三个测试链表添加至链表数组
        ListNode node1 = new ListNode(1);
        node1.next = new ListNode(4);
        node1.next.next = new ListNode(5);

        ListNode node2 = new ListNode(1);
        node2.next = new ListNode(3);
        node2.next.next = new ListNode(4);

        ListNode node3 = new ListNode(2);
        node3.next = new ListNode(6);

        ListNode[] lists = {node1, node2, node3};

        Solution result = new Solution();
        ListNode res = result.mergeKLists(lists);;

        result.showListNode(res);
    }
    
}

