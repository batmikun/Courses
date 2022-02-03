# Refactoring

The main purpose of refactoring is to fight technical debt. It transfroms a mess into clean code and simple design.

# Clean Code

-   Clean Code is obvious for other programmers.

    1.  Poor variables naming, bloated classes and methods, magic numbers -you name it- all of that makes code sloppy and difficult to grasp.

-   Clean code doesn't contain duplication.

    1.  Each time you have to make a change in a duplicate code, you have to remember the same change to every instance. This increases the cognitive load and slows down the progress.

-   Clean code contains a minimal number of classes and other moving parts.

    1.  Less code is less stuff to keep in your head.
    2.  Less code is less maintenance.
    3.  Less code is fewer bugs.
    4.  Code is liability, keep it shor and simple.

-   Clean code is easier and cheaper to maintain!

# Technical Debt

-   You can temporarily speed up without writing tests for new features, but this will gradually slow your progress every day until you eventually pay off the debt by writing tests.

-   Causes:
    1.  Business Pressure.
    2.  Lack of understanding of the consequences of technical debt.
    3.  Failing to combat the strict coherence of components.
        -   This is when the project resembles to a monolith rather than the product of individual modules. In this case, any changes to one part of the project will affect others
    4.  Lack of tests
    5.  Lack of documentation
    6.  Lack of interaction between team members
    7.  Long-term simultaneous development in several branches
    8.  Delayed refactoring
    9.  Lack of compliance monitroing
    10. Incompetence

# When to refacor?

    RULE OF THREE:
        1.  When you're doing something for the first time, just get it done
        2.  When you're doing something similar for the second time, cringe at having to repeat but do the same thing anyway
        3.  When you're doing something similar for the third time, start refactoring.

    When adding a feature
        1. Refactoring helps you understand other people's code. If you have to deal with someone else's dirty code, try to refactor it first. Clean code is much easier to grasp. You will improve in not only for yourself but also for those who use it after you
        2. Refactoring makes it easier to add new features. It's much easier to make changes in clean code.

    When fixing a bug
        1. Bugs in code behave just like those in real life: they live in the darkest, dirtiest places in the code. Clean your code and the error will practically discover themselves.
        2. MAnagers appreciate proactive refactoring as it eleiminates the need for special refactoring task later.

    During a code review
        1. Code reviews are a great way to learn about other people's code.
        2. Code reviews are a great way to learn about your own code.
        3. Code reviews are a great way to learn about the code you're working on.

# HOW TO REFACTOR

-   Checklist of refactoring done right way:
    -   The Code Should Become Cleaner
    -   New Functionality shouldn't be created during refactoring.
    -   All existing tests must pass after refactoring

# CODE SMELLS

-   BLOATERS:

    -   Code, methods and classes that have increased to such enormous proportions that they are hard to work with. Usually these smells do not croup up right away, rather they accumulate over time as the program evolves

        1.  Long Method -> any method longer than 20 lines should make you start asking questions about whether it should be split into smaller methods.

        2.  Large Class -> a class contains many fields/methods/lines of code

        3.  Primitive Obsession

            -   Use of primitives of small object for simple tasks (currency, ranges, special string for phone numbers, etc.).
            -   Use of constans for coding information (USER_ADMIN_ROLE = 1)
            -   Use of string constants as field names for use in data arrays

        4.  Long Parameter List -> Mora than three or four parameters for a method

        5.  Data Clumps -> Sometimes different parts of the code contain identical groups of variables (database parameters). These clumps should be turnes into their own classes.

-   OBJECT-ORIENTED ABUSERS:

    -   All these smells are incomplete or incorrect application of oop principles

        1.  Alternative Classes with different interfaces -> Two classes perform identical functions but have different method names

        2.  Refused Bequest -> If a subclass use only some of the methods and properties inherited from its parents, the hierarchy is off-kilter. The unneeded methods my simply go unused or be redefined and five off exceptions.

        3.  Switch Statements -> You have a complex switch or sequence of if statements.

        4.  Temporary Field-> Temporary fields get their values (and thus are needed by objects) only under certain circumstances. Outside of these cirucmstances, they are empty.

-   CHANGE PREVENTERS:

    -   These smells mean that if you need to change something in one place in your code, you have to make many changes in other places too. Program development becomes much more complicated and expensive as a result

        1.  Divergent Change -> You find yourself having to change many unrelated methods when you make changes to a class. For example, when adding a new product type you have to change the methods for finding, displaying, and ordering products.

        2.  Parallel Inheritance Hierarchies -> Whenever you create a subclass for a class, you find yourself needing to create a subclass for another class.

        3.  Shotgun Surgery -> Making any modifications requires that you make many small changes to many different classes.

-   COUPLERS:

    -   All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation

        1.  Feature Envy -> A method accesses the data of another object more than its own data.

        2.  Inappropriate Intimacy -> One class uses the internal fields and methods of another class.

        3.  Incomplete library class -> Sooner or later, libraries stop meeting user needs. The ony solution to the problem -changing the library- is often impossible since the library is read-only.

        4.  Message Chains -> In code you see a series of call resembling $a->b()->c()->d()

        5.  Middle Man -> If a class performs only one action, delegating work to another class, why does it exist at all?

# REFACTORING TECHNIQUES
