# Hexagonal Architecture

# DDD - Domain Driven Design

# Tactial Design

Model-Driven Design

1. Expressed with:

-   Services
-   Domain Events
-   Entites
-   Value Objects

    Entities:

    -   Publishes state changes in:
        -   Domain Events
    -   Integrity maintained by:
        -   Aggregates
    -   Accesed using:
        -   Repositories

    Value Objects:

    -   Encapsulated with:
        -   Aggregates
        -   Factories

    Aggregates:

    -   Accesed using:
        -   Repositories
    -   Encapsulated with:
        -   Factories

2. Isolated with:

-   Layered Architecture:
    -   Domain Layer
    -   Infrastructure Layer
    -   Application Layer

3. Gives Structure to:

-   Ubiquitous Language

4. Defined Within:

-   Bounded Context:
    -   Ubiquitous Language

# Strategic Desing

Model-Driven Design

-   Gives structure to

    -   Ubiquitous Language

-   Defined Within:

    -   Bounded Context:
        Names enter:

        -   Ubiquitous Language

        Keep model unified by:

        -   Continoous Integration

        Overview relationships with:

        -   Context Map

            Overlap Contexts though:

            -   Shared Kernel

            Relate Contexts as:

            -   Customer/Supplier Teams

            Segregate Conceptual Messes:

            -   Big Ball Of Mud

            Translate And Insulate With:

            -   Anticorrption Layer

            Free teams to:

            -   Separate Ways

            Support Multiple Clients though:

            -   Open Host Service

            Formalize as:

                -    Published Language

# STRUCTURE OF ALL CLEAN ARCHITECTURES

Outter Layer:

-   Devices
-   Db
-   External Interfaces
-   Web
-   UI
-   Frameworks

In the outter layer is where we implement the logic. We can think it as the controller of a symfony application, we will call our repositories, do stuff, and return the result to the view.

3 Layer:

-   Controllers
-   Gateways
-   Presenters

2 Layer:

-   Use Cases

Inner Layer:

-   Entities

# STRUCTURE OF HEXAGONAL ARCHITECTURES

Outter Layer:

-   Framework / Infrastructure

For example the class that implements the interface to register a user, and the controller that call that class and implement the logic.

Middle Layer:

-   Application

Use Cases, the connection between the Domain and the Infrastructure.
Because in here, we are gonna have class that implment the logic, and the things that we define in our domain. But we only pass interfaces here, the implementation is in the Infrastructure Layer.

Inner Layer:

-   Domain

For example the object that represents the user
For example the interface that represents a repositorie

# Definitions

-   Domain Model:

    -   A Domain Model creates a web of interconnected objects, where each object represents some meaningful individual, whether as large as a corporation or as small as a single line on an order form.

-   Bounded Context:

    -   It is the focus of DDD's strategic design section which is all about dealing with large models and teams. DDD deals with large models by dividing them into different Bounded Contexts and being explicit about their interrelationships.
        Example of Bounded Context:
    -   Sales Context
    -   Support Context

    Basically is a group of things that represents a single area of the company.

-   Ubiquos Language:

    -
