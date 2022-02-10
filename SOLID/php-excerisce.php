<?php

// DOMINIO

interface OperationsForAccounts
{
    public function __construct(float $balance);

    public function calculateInterest(): float;
}

class SavingAccount implements OperationsForAccounts
{
    public function __construct(float $balance)
    {
        $this->balance = $balance;
    }

    public function calculateInterest(): float
    {
        return $this->balance * 0.3;
    }
}

class FixedDepositAccount implements OperationsForAccounts
{
    public function __construct(float $balance)
    {
        $this->balance = $balance;
    }

    public function calculateInterest(): float
    {
        return $this->balance * 0.9;
    }
}

class OperationsForAccountsFactory
{
    public static function create(string $type, float $balance): OperationsForAccounts
    {
        switch ($type) {
            case 'saving':
                return new SavingAccount($balance);
            case 'fixed':
                return new FixedDepositAccount($balance);
            default:
                throw new Exception('Invalid account type');
        }
    }
}

// FIN DEL DOMINIO

// CASOS DE USO

class InterestCalculator

{
    public function calculate(string $accountType, int $accountBalance): float
    {
        $operationsAccountFactory = OperationsForAccountsFactory::create($accountType, $accountBalance);

        return $operationsAccountFactory->calculateInterest();
    }
}

// FIN DE CASO DE USO

// IMPLEMENTACION

$interestCalculator = new InterestCalculator();

echo $interestCalculator->calculate('saving', 1000);
echo $interestCalculator->calculate('fixed', 1000);
