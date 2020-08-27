<?php

class Solution {

    /**
    * @param Integer[] $nums
    * @param Integer $target
    * @return Integer[]
    */
    function twoSum($nums, $target) {
        $m = [];
        foreach ($nums as $k => $v) {
            if (isset($m[$target-$v])) {
                return [$m[$target-$v], $k];
            }
            $m[$v] = $k;
        }
    }
}

$obj = new Solution();
print_r($obj->twoSum([1,2,3], 5));