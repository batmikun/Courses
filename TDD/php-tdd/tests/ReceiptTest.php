<?php

namespace TDD\tests;

require dirname(dirname(__FILE__)) . DIRECTORY_SEPARATOR . 'vendor' . DIRECTORY_SEPARATOR . 'autoload.php';

use PHPUnit\Framework\TestCase;
use TDD\Receipt;

class ReceiptTest extends TestCase
{
    protected function setUp(): void
    {
        $this->formatter = $this->getMockBuilder('TDD\Formatter')
            ->onlyMethods(['currencyAmount'])
            ->getMock();

        $this->formatter->expects($this->any())
            ->method('currencyAmount')
            ->with($this->anything())
            ->will($this->returnArgument(0));

        $this->receipt = new Receipt($this->formatter);
    }

    protected function tearDown(): void
    {
        unset($this->receipt);
    }

    /**
     * @dataProvider provideTotal
     */
    public function testTotal($items, $expected)
    {
        $coupon = 0.0;
        $result = $this->receipt->total($items, $coupon); // act
        $this->assertEquals( // assert
            $expected,
            $result,
            "Total should be {$expected}"
        );
    }

    public function provideTotal()
    {
        return [
            "Data Set 1" => [
                [7, 7],
                14,
            ],
            "Data Set 2" => [
                [7, 7, 7],
                21,
            ],
            "Data Set 3" => [
                [7, 7, 7, 7],
                28,
            ],
        ];
    }

    public function testTotalWithCouponDifferentFromNull()
    {
        $items = [7, 8]; // arange
        $coupon = 0.20;
        $result = $this->receipt->total($items, $coupon); // act
        $this->assertEquals( // assert
            12,
            $result,
            'Total should be 12'
        );
    }

    public function testTotalException()
    {
        $items = [7, 8]; // arange
        $coupon = 1.20;
        $this->expectException('BadMethodCallException');
        $this->receipt->total($items, $coupon); // act
    }

    public function testPostTaxTotal()
    {
        $items = [1, 2, 5, 8];
        $tax = 0.20;
        $coupon = null;

        $receipt = $this->getMockBuilder('TDD\Receipt')
            ->onlyMethods(['taxes', 'total'])
            ->setConstructorArgs([$this->formatter])
            ->getMock();

        $receipt->expects($this->once())
            ->method('taxes')
            ->with($this->equalTo(10), $this->equalTo($tax))
            ->willReturn(1.00);

        $receipt->expects($this->once())
            ->method('total')
            ->with($items, $coupon)
            ->willReturn(10.00);

        $result = $receipt->postTaxTotal($items, $tax, $coupon);

        $this->assertEquals(
            11.00,
            $result,
            'Post tax total should be 11.00'
        );
    }

    public function testTaxes()
    {
        $amount = 100.00;
        $taxesPercent = 0.10;
        $result = $this->receipt->taxes($amount, $taxesPercent);

        $this->assertEquals(
            10.00,
            $result,
            'Taxes should be 10.00'
        );
    }
}
