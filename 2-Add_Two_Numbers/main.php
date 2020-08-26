<?php
/**
 * Definition for a singly-linked list.
 */
class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}
class Solution {

    /**
     * 36ms
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $head = new ListNode();
        $prev = $head;
        $carry = 0;
        while (!empty($l1) || !empty($l2)) {
            $addition = $l1->val+$l2->val+$carry;
            $carry = floor($addition/10);
            $l1 = empty($l1->next) ? NULL : $l1->next;
            $l2 = empty($l2->next) ? NULL : $l2->next;

            $curr = new ListNode($addition%10);
            $prev->next = $curr;
            $prev = $curr;
        }
        if ($carry > 0) {
            $prev->next = new ListNode($carry);
        }
        return $head->next;
    }
}

