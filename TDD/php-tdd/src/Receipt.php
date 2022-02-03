<?php

namespace TDD;

use BadMethodCallException;

class Receipt
{

    public function __construct($formatter)
    {
        $this->formatter = $formatter;
    }

    public function total(array $items, ?float $coupon): float
    {
        if ($coupon > 1.00) {
            throw new BadMethodCallException('Coupon must be between 0 and 1');
        }

        $sum = array_sum($items);

        return $sum - ($coupon * $sum);
    }

    public function taxes(float $amount, ?float $taxesPercent): float
    {
        return $this->formatter->currencyAmount($amount * $taxesPercent);
    }

    public function postTaxTotal(array $items, float $taxesPercent, ?float $coupon): float
    {
        $subtotal = $this->total($items, $coupon);

        return $subtotal + $this->taxes($subtotal, $taxesPercent);
    }
}
