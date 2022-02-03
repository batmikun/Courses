<?php

namespace TDD\tests;

require dirname(dirname(__FILE__)) . DIRECTORY_SEPARATOR . 'vendor' . DIRECTORY_SEPARATOR . 'autoload.php';

use PHPUnit\Framework\TestCase;
use TDD\Formatter;

class FormatterTest extends TestCase
{
    public function setUp(): void
    {
        $this->formatter = new Formatter();
    }

    public function tearDown(): void
    {
        unset($this->formatter);
    }

    /**
     * @dataProvider provideCurrencyAmount
     */
    public function testCurrencyAmount($input, $expected, $message)
    {
        $this->assertSame(
            $expected,
            $this->formatter->currencyAmount($input),
            $message
        );
    }

    public function provideCurrencyAmount()
    {
        return [
            [1, 1.00, '1 should be transformed into 1.00'],
            [1.1, 1.10, '1.1 should be transformed into 1.10'],
            [1.11, 1.11, '1.11 should be transformed into 1.11'],
            [1.111, 1.11, '1.111 should be transformed into 1.11']
        ];
    }
}
