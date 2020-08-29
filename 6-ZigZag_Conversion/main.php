<?php

class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        if ($numRows <= 1) {
            return $s;
        }

        $m = [];
        for ($i=0; $i<$numRows; $i++) {
            $m[$i] = '';
        }
        $i = 0;
        $n = -1;
        for ($j=0; $j<strlen($s); $j++) {
            $m[$i] .= $s[$j];
            if ($i == 0 || $i == ($numRows-1)) {
                $n = -$n;
            }
            $i += $n;
        }
        $ret = '';
        foreach ($m as $j) {
            $ret .= $j;
        }
        return $ret;
    }
}

$obj = new Solution();
echo $obj->convert('PAYPALISHIRING', 0);
