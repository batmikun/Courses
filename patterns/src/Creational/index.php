<?php

namespace patterns\Creational;

use patterns\Creational\SimpleFactory\VehicleFactory;

require __DIR__ . '/../../vendor/autoload.php';

function SimpleFactory()
{
    $Luxury = VehicleFactory::gerVehicle('Luxury');

    $LowCost = VehicleFactory::gerVehicle('LowCost');

    echo $Luxury->call();

    echo $LowCost->call();
}

SimpleFactory();
