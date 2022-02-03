<?php

namespace patterns\Creational\SimpleFactory\Interfaces;

abstract class AbstractVehicles
{
    protected $cars = [];

    public function __construct(array $cars)
    {
        $this->cars = $cars;
    }

    abstract public function call();
}
