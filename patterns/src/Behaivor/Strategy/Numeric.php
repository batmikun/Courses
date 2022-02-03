<?php

namespace patterns\Behaivor\Strategy;

use patterns\Behaivor\Strategy\ValidationInterface;

class Numeric implements ValidationInterface
{
    private $value;
    private $name;

    public function __construct(string $value, string $name)
    {
        $this->value = $value;
        $this->name = $name;
    }

    public function validate(): string
    {
        if (filter_var($this->value, FILTER_VALIDATE_INT)) {
            return "$this->name is valid";
        }

        return "$this->name is not valid";
    }
}
