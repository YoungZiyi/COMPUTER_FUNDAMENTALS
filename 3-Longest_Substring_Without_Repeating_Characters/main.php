<?php
class Solution {
    /**
     * sliding wiindow
     * 24ms
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        if (empty($s)) {
            return 0;
        }
        $index = [];
        $max_length = $left = $right = 0;
        foreach (str_split($s) as $k => $c) {
            $right = $k;
            if (isset($index[$c]) && $left <= $index[$c]) {
                $left = $index[$c] + 1;
            }
            $index[$c] = $k;
            $curr = $right - $left + 1;
            $max_length = ($curr > $max_length) ? $curr : $max_length;
        }
        return $max_length;
    }
}
$obj = new Solution();
echo $obj->lengthOfLongestSubstring('abb');