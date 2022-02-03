<?php

namespace patterns\Creational\SimpleFactory;

use patterns\Creational\SimpleFactory\Interfaces\AbstractVehicles;

class LowCost extends AbstractVehicles
{
    public function call()
    {
        echo 'A' . $this->cars[array_rand($this->cars)] . ' is a low cost car.';
    }
}
