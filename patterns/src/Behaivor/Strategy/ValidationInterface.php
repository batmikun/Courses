<?php

namespace patterns\Behaivor\Strategy;

interface ValidationInterface
{
    public function __construct(string $value, string $name);

    public function validate(): string;
}
