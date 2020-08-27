<?php
class Solution {

/**
 * @param Integer[] $nums1
 * @param Integer[] $nums2
 * @return Float
 */
function findMedianSortedArrays($nums1, $nums2) {
    $total = count($nums1) + count($nums2);
    $mid = floor($total/2);
    $first = $second = 0;
    for ($i=0; $i<=$mid; $i++) {
        $second = $first;
        if (empty($nums1)) {
            $first = array_pop($nums2);
        } else if (empty($nums2)) {
            $first = array_pop($nums1);
        } else {
            $first = (end($nums1) > end($nums2)) ? array_pop($nums1) : array_pop($nums2);
        }
    }
    return ($total%2) ? $first : round(($first+$second)/2, 5);
}
}
$obj = new Solution();

// $nums1 = [1,3];
// $nums2 = [2];

// $nums1 = [1,2];
// $nums2 = [3,4];

// $nums1 = [0,0];
// $nums2 = [0,0];

$nums1 = [];
$nums2 = [1];

$nums1 = [];
$nums2 = [];

echo $obj->findMedianSortedArrays($nums1, $nums2);