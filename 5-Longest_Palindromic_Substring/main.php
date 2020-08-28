<?php

class Solution {

/**
 * @param String $s
 * @return String
 */
function longestPalindrome($s) {
    $total = strlen($s);
    if ($total <= 1) {
        return $s;
    }
    $ret = $s[0];
    for ($i=0; $i<($total-1); $i++) {
        $tmp1 = $this->centralCheck($s, $i, $i);
        $tmp2 = $this->centralCheck($s, $i, $i+1);
        $tmp = strlen($tmp1)>strlen($tmp2) ? $tmp1 : $tmp2;
        $ret = strlen($tmp)>strlen($ret) ? $tmp : $ret;
    }
    return $ret;
}

function centralCheck($s, $i, $j) {
    $ret = $s[$i];
    while ($i>=0 && $j<strlen($s)) {
        if ($s[$i] != $s[$j]) {
            break;
        }
        $ret = substr($s, $i, $j-$i+1);
        $i--;
        $j++;
    }
    return $ret;
}
}

$obj = new Solution();
echo $obj->longestPalindrome('bb');