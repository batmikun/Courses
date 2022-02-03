<?php

namespace TDD;

class Formatter
{
    public function currencyAmount(float $amount): float
    {
        return round($amount, 2);
    }
}
