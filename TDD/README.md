# TDD

-   Ensures it works correctly now and in the future
-   Additional documentations into what your code does
-   Reduces the chance of bugs or issues
-   Improves ability to refactor your code
-   Forces you to write better designed code

# Structuring Test Cases

Typically, one test class per code class, however

-   One test class may test more than one code class
-   One code class may be tested by more than one test class
-   Design test cases to test requirements, not to test methods

-   Provides instant feedback on the correctness of the code
-   Helps to identify bugs in the code, because we develop the test cases before the code

# Test-Last Development

Requirements -> Design -> Code -> Test

# Test-First Development

Requirements -> Test -> Design -> Code

With the requeriements, we can design the test cases. And the design of the application is born from the test cases.

This is the pure approach of TDD.

Testing in TDD -> Is only about UNIT TESTING -> Testing the smallest unit possible

# Test-First Development

When we have larger projects or requirements, sometimes is difficult to divide things into smaller pieces.

In this cases we probably come-up with some part of the desing first, and then we can test it.

Requirements -> Design -> Test -> Code

TFD and TDD overlap each other.

# TDD

The cycle of TDD is:

1. Test Case
2. Code
3. Refactor

# Refactoring : Changing internal structure of software to make it easier tounderstand and cheaper to modify without changing its external behavior.

# THE GOLDEN RULE IN TDD IS BEFORE WRITING A SINGLE LINE OF CODE, CREATE THE TEST CASE

# UNIT LIBRARY -> Core Components

1. Test Case
2. Test Fixtures
3. Test Suite
4. Test Runner
5. Test Result

# WRITING TEST CASES

EXAMPLE

-   Requirement : How many times an alphabet appears in a word
-   Word: pizza
-   Alphabet: z -> Count: 2
-   Alphabet: x -> Count: 0

The name of the methods has to be very explicit.
It doesn't matter if the name is to long

# IDEAL ESCENARIO

1. Write a failing test case
2. Code to pass the test
3. Refactor

# The idea is to start small

This means that our methods should be small and simple.
If we have a test for a method that returns certain word.
When we create the method in the class, we can hardcode the
returned word to pass the test. It's okay to do that

Then we can go increasing the difficulty of the test, and in that way we model our method to adjust to the test.

# Where to Start? Best Practices

-   Prioritize use cases in sprint planning
-   Identify the acceptance criteria
-   Start with unit test cases for the acceptance criteria

# TDD Cycle

1. Write a failing test case
2. Code to pass the test
3. Refactor

# Refactoring

Changing internal structure of software to make it easier to
understand and cheaper to modify without changing its external
behavior.

Refactoring becomes very easy in TDD because we have the test cases to be safe.

To know when to refactor, we have to be able to detect code smells.

For example if we have a method that the responsability is to fetch a word, but we have the logic to load the word from a file inside of that method. We can refactor to move out the logic to a different method. And in the method fetchAWord only leave the responsability to return the word.

When we refactor, we DO NOT add Adding new functionality.
We only Improved Code.

# Structuring Test Cases

-   Typically, one test class per code class, however
-   When it becomes to large, we divide that class in smaller class

# TEST FIXTURE

-   A fixed state of the system required at the start of a test
-   Ensure that a test is repeatable
-   Set up before the test runs and torn down after is has finished
-   Can be shared by test cases needing the same state

-   This is called SetUpTearDown Pattern

# ASSERTIONS

-   Assertion: and idiom for defensive programming
-   Supported in many languages, including C, C++, Java, JavaScript, Python, PHP
-   Has a condition that is expected to be true when executed, else it throw an assertion error
-   There a multiple types of assertions:
    1. assertTrue(condition)
    2. assertFalse(condition)
    3. assertEquals(expected, actual)
    4. assertNotEquals(expected, actual)
    5. assertNull(object)
    6. assertNotNull(object)
    7. assertSame(expected, actual)
    8. assertNotSame(expected, actual)
    9. assertArrayEquals(expected, actual)
    10. assertThrows(exception, method)
    11. assertThat(actual, matcher)

All the assertions that have a message paramater that is optional.
This message is displayed when the codition is not met

The difference between same and equals is that same is used to compare references, and equals is used to compare values.

# Testing Exceptions

-   When we have test cases that have to test methods exceptions
-   We have to desing the test cases a little bit differently
-   For this methods we use assertThrows

# Test Case Pattern

The patterns of the test cases generally are:

    1. Arrange -> Setup all the data and object necessary to test the functionallity
    2. Act -> Execute the functionallity that we want to test
    3. Assert -> Verify that the functionallity has the expected result

This pattern is called Arrenge-Act-Assert

Generally the part that most repeat is the Arrange part.
To avoid this type of repetition, we use the Test Fixture Pattern.

# TEST FIXTURE

-   A fixed state of the system required at the start of a test
-   Ensure that a test is repeatable
-   Set up before the test runs and torn down after is has finished
-   Can be shared by test cases needing the same state

-   This is called SetUpTearDown Pattern

To mantain and scale out TDD, we use frameworks and tools, that help us to organize our tests. And making our tests more readable.
Also we use Mocking frameworks to help test external dependencies of the system under test.

External dependicies can be databases, webservices or other systems.

We can use proxys to mock the external dependencies.

This is called TEST DOUBLES

# Test Doubles

A generic term for any case where you replace a production object for testing purposes.

    Mayor three cases when we are gonna use test doubles:
        Replace dependencies
        Ensure a condtion occurs
        Improve the performance of out tests

1. Dummy object
   Is a object that does not do anything. And generally is part of a parameter for a function or method.

2. Stub object
   Returns a preset value
   Is a mock object that does not do anything but has logic. But intends to replace the logic of the object that communicates with the storage.
   It's a Hand Coded class, for example this is the type of class that will return
   a hard-coded object or a hard-coded value.
   This offers canned responses (hard-coded)
   Focuses on state of the dependency

3. Mock object
   Ojectes pre-programmed with expectations which form a specefication of the calls the are expected to recieve.
   This code is generated, it's not hand-coded, using a mocking framework. We do not code a mock
   This offers expected behavior (mock)
   Fully focuses on behavior of the dependency

4. Fake object
   Simplefied version of the real object.
   We can apply logic to an dummy or stub object. But is fake. For example we want to check that the method returns true, so inside the method we put only a return true;

5. Spy object
   A spy acts as a higher level stub, it allows us to also record information about what happened with this test double. For example, we can record the calls to the method.

# General Principles

-   Test in isolation
-   Test only a few things at once or even just one thing at once
-   Test should be easy to write, a hard test generally means re-write your implementation

In php unit, we have the functions:

1.  setUp : void -> This method is called before each test
2.  tearDown : void -> This method is called after each test

    To run all the test in PHPUnit, we have to use the command:

        vendor\bin\phpunit tests This will run all the tests inside the tests folder

    To run a specific test, we have to use the command:

        vendor\bin\phpunit tests/Unit/ExampleTest.php

    Or we can run only a directory inside the tests folder:

        vendor\bin\phpunit tests/Unit

    Also we can use a filter parameter:

        vendor\bin\phpunit tests/Unit --filter=testName or testClassName::testName

    We can also add a xml file to configure how we want to run the tests, when we do this, we create a file called phpunit.xml in the root of the project. And the call the command:

        vendor\bin\phpunit

    We can call specific testsuites doing this:

        vendor\bin\phpunit --testsuite=testsuiteName

# Mocks in phpUnit

    To create a mock for a class:

        $mock = $this->getMockBuilder('ClassName')->getMock();

        We can specify the methods that we want to mock. With the onlyMethods() method.

        Then we have to build that methods.
            $mock->expects($this->once())->method('methodName')->willReturn(true);

        Also we can add parameters to those mock methods with the methods with(parameters)

        The mocks give us also the ability to test the methods that we are mocking. So we are able to define the type and the value of the parameters.

# Data Providers

-   Test multiple inputs to a method without duplicate a bunch of code

-   To create a data provider we can add a comment with the name of the data provider after the name of the testfunction.

    /_
    @dataProvider additionProvider
    _/
    public function testAdd($a, $b, $expected)
    {
        $calculator = new Calculator();
        $this->assertEquals($expected, $calculator->add($a, $b));
    }

    Then we have to create a method with the name of the data provider. And return an array with the values that we want to test.

    public function additionProvider()
    {
    return [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 2],
    [1, -1, 0],
    [-1, 1, 0],
    [-1, -1, -2]
    ];
    }

# Code Coverage

    What percetange of lines in our code base is cover by tests?
    What lines were run for what tests?

# Test Databases

    We usually test database with Fixtures.

    Fixture is a set of data that we can use to test our code.

    It can be a class that share the same interfaces of the database.

    So it'll have the same methods and the same properties that te real class

    and then build a mock class of that fixture
