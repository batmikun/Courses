//SPDX-License-Identifier: MIT

pragma solidity >=0.4.0;

/* 
    We can test in the JMV 

    The first thing we do is to specify the version of solidity that we are going tu use
    the version is tied up with the version of the compiler that we are using

    To make a contract we simple create a "class"

    contract SimpleStorage {

    }

    Like a class we have properties and methods
    the methods to be visibilize are EXTERNAL, PUBLIC
    PRIVATE, INTERNAL

    EXTERNAL -> Cannot be call by the same contract, it has to be call from another contract
    INTERAL -> Can be call by functions in the same contract

    If we don't define the visibility in variables or methods automcally
    become INTERNAL

    DATA TYPES

    We have many different types

    The best practices is to use the hole name
    instead of unit do uint256

    TYPE VISIBILITY VARIABLENAME = VALUE

    int
    uint -> thay are not positive or negative
    uint256 -> 256 bits
    bool favoriteBool = false;
    string favoriteString = "String";
    int256 favoriteInt = -5;
    address favoriteAddress = 0x0; -> ETH address
    bytes32 favoriteBytes = "cat"; -> 32 bytes

    functions -> we define with the keyword function

    KEYWORD (FUNCTION) FUNCTIONNAME (TYPE PARAMETER) KEYWORD (PUBLIC OR PRIVATE, ETC) {
        CODE
    }

    function store(uint256 _x) public {
        x = _x;
    }

    Also we can have

    FUNCTION STORE (TYPE PARAMETER) PUBLIC VIEW RETURNS(TYPE RETURN) {
        CODE
    }

    if we add view to the function this mean that we are reading from the blockchain
    that means that we dont have to pay a gas fee for interacting with that fucntions

    the same goes for public pure -> this is used to do calculations and thing like that

    VIEW - PURE -> don't cost gas

    STRUCTS -> Create a new type

    struct People {
        string name;
        uint age;
    }

    People person = People("John", 30);

    ARRAYS -> Stores a list of values

    People[] people;

    We add things to the array with the push function

    people.push({
        name: "John",
        age: 30
    });

    We can store things in memory or storage
    we define this in the parameter of the function

    memory -> it keeps the volue only during the execution
    generally we use memory with string

    function store(string memory _hola) public {
        hola = _hola;
    }

    MAPPINGS -> Stores a list of key => values. This is something like a dict en python or an associative arrays in PHP

    mapping(typeKey => typeValue) visibility nameoftheDict

    mapping(string => uint256) public nameToFavoriteNumber;

    add something

    nameToFavoriteNumber["John"] = 30;
*/

contract SimpleStorage {
    uint256 favoriteNumber; // if we dont specify the value its gonna inicialize to 0 or default value

    struct People {
        // Like in TS
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
