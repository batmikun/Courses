<?php
function solution($str)
{

    $list = array();

    $isOdd = strlen($str) % 2;

    for ($i = 0; $i < strlen($str); $i = $i + 2) {
        if ($isOdd != 0 && $i == strlen($str) - 1) {
            $list[] = $str[$i] . "_";
        } else {
            $list[] = $str[$i] . $str[$i + 1];
        }
    }

    return $list;
}

var_dump(solution("abc"));
