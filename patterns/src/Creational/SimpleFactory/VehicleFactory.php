<?php

namespace patterns\Creational\SimpleFactory;

use patterns\Creational\SimpleFactory\Interfaces\AbstractVehicles;
use patterns\Creational\SimpleFactory\LowCost;
use patterns\Creational\SimpleFactory\LuxuryCost;

class VehicleFactory
{
    static public function gerVehicle($type): AbstractVehicles
    {
        switch ($type) {
            case 'Luxury':
                return new LuxuryCost(['BMW', 'Mercedes', 'Audi']);
            case 'LowCost':
                return new LowCost(['Volvo', 'Ford', 'Nissan']);
            default:
                throw new \Exception('Vehicle not found');
        }
    }
}
