<?php

namespace patterns\Creational\SimpleFactory;

use patterns\Creational\SimpleFactory\Interfaces\AbstractVehicles;

class LuxuryCost extends AbstractVehicles
{
    public function call()
    {
        echo 'A' . $this->cars[array_rand($this->cars)] . ' is a luxury car.';
    }
}
