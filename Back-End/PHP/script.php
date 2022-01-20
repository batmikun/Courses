<?php
function Limiter(int $n): int
{
    if ($n == 6) {
        return 3;
    } else {
        return 3 * Limiter($n + 1);
    }
}

echo Limiter(3);
