package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"sort"
	"strconv"
	"strings"
)

/**

Go is a statically typed language.

	The basic data types are:
		bool
		string
		int8, int16, int32, int64
		uint8, uint16, uint32, uint64
		float32, float64
		complex64, complex128 -> complex numbers (real and imaginary parts)

	Data Collections:
		Array
		Slice
		Map
		Struct

	Language Organization:
		Functions
		Interfaces
		Channel

	Data management:
		Pointers

	Functions are first class citizens.
*/

/**
Variables -> You can specify the types of variables or let the compiler infer the type.

	var name = value
	var name type = value

	const name type = value

	another way of creating a variable is:

		name := value -> this only works inside a function.

		You cannot define the type
*/

/**
Reading input from the user

	To read input from the user, we use the bufio package.
	we have to create a redaer object and then call the ReadString method.

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter your name: ")

	This function returns to values, the input and the error
	if we wanna ignore a variable we call it with _

	input, _ := reader.ReadString('\n')

	When we ask input to the user is always wanna be a string

	If we wanna convert the string to a int we do

		aFloat, err := strconv.ParseFloat(strings.TrimSpace(numInput), 64)

		if err != nil { We know we have an error when in the variable the result is different to nil
			fmt.Println(err)
		}

		fmt.Println(aFloat)

*/

/**
Math Operators

	+ -> Addition
	- -> Subtraction
	* -> Multiplication
	/ -> Division
	% -> Modulus
	** -> Exponentiation
	& -> Bitwise AND
	| -> Bitwise OR
	^ -> Bitwise XOR
	<< -> Bitwise Left Shift
	>> -> Bitwise Right Shift
	&^ -> Bitwise AND NOT

	We cannot do operations between int and float, we have to convert one of the values to the other type

	For math operations we use the package math

*/

/**
Arrays and Slices

	Arrays are fixed size, slices are variable size

	Arrays

		var name [size]type = [size]type{value1, value2, value3, ...}

		We can modify the values in the array, but we cannot add or remove elements

	Slices

		var name []type = []type{value1, value2, value3, ...}

		The only difference with arrays is that we can add and remove values
*/

/**
Loops

	We use the word for to create a loop.

	If we want a "while"

	for condition {}

	A normal one

	for i := 0; i < 10; i++ {}

	Loop trhoug an array or slice

	for i := 0; i < len(array); i++ {}

	We do a foreacb tbis way ("foreach" in js or "for in" in python)

	for index, value := range names {}

	If we don't wanna use index we replace it with _ (with _ we are telling GO that ignore that variable)

	goto label -> Go to a specific label
	label -> Label for a specific point in the code
*/

/*
LABELS

	We use the word label to create a label for a specific point in the code.

	Example :
		- We have a for loop that we want to break out of.
		- We have a for loop that we want to continue.

	for i := 0; i < 10; i++ {
		if i == 5 {
			goto breakHere
		}

		fmt.Println(i)
	}

	breakHere: // This is the label
*/

/**

Functions

	We define functions with the keyword "func"

	func name(parameters) returnType {}

	we only have to specify the return type when the function returns something if the function
	only cause a side-effect or void we can define it

	func name(parameters) {}

	We can returns other functions or pass functions as parameter or store functions in variables

	To pass a function as a parameter

		func name(f func(type)) returnType {}

Returning multiple values

	We can also return multiple values in a single line
	but we have to specify the type of each value

	func name(parameters) (returnValueType1, returnValueType2, returnValueType3) {}

	We can also return multiple values in a single line
	We are gonna have the same amount of returnTypes as returnValues doesn't matter if we return to string
	we hace to specify (string, string)

	func getInitials(n string) (string, string) {
		n = strings.ToUpper(n)
		names := strings.Split(n, " ")

		var initials []string
		for _, value := range names {
			initials = append(initials, string(value[:1]))
		}

		if len(initials) == 1 {
			return initials[0], ""
		}

		return initials[0], initials[1]
   	}

	To obtain the result of a function with multiple returns we do

	   firstInitial, secondInitial = getInitials("John Doe")

	If we have multiple parameters of the same type we can use ... to indicate that we can pass as many
	as we want. Is like *args in python

	func sum(numbers ...int) int {
		var sum int = 0
		for _, value := range numbers {
			sum += value
		}

		return sum
	}

	sum(1, 2, 3, 4, 5)

	DEFER -> We use the keyword defer to execute a function at the end of the function

	func main() {
		resp, err := http.Get("http://www.google.com")

		if err != nil {
			panic(err)
		}

		fmt.Printf("%s", resp.Body)

		defer resp.Body.Close()
	}

	The defer keyword is gonna wait until all the operations af the functions are done to run the statement

	It's helpful when we are working with files, to close the files or http request, etc
*/

/*
Pass parameters by value or reference

	We can pass parameters by value, the value is copied to the function
	and the original value is not modified.
	This happens with these types:
	   	int, float, string, bool, complex64, complex128
		uint, Array, Structs ->
		They are called Non-Pointer Values


	We can also pass parameters by reference, the value is a reference to the
	original value.
	This happens with these types:
	   	slice, map, pointer, channel, functions ->
		They are called Pointer Values

	If we want to pass a Non-Pointer Value as a Pointer Value we have to use the & operator

	func main() {
		name := "Tifa"

		updateName(&name)
	}

	When we have a pointer

	m := &name -> This is type of pointer

	To obtain the value we have to do

	println(*m)
*/

/*
MEMORY ALLOCATION

	We can use the keyword "new" or "make" to create complex types such as Slices, Maps, Channels, Functions

	We use the keyword "new" to allocate memory for a variable
		- Allocates by does not initialize the memory
		- Results in zeroed storage but returns a memory address
		- If we try add a value to the variable we will get an error

	We use the keyword "make" to allocate memory for a variable
		- Allocates and initializes the memory
		- Allocates non-zeroed storage and returns a memory address

	m := new(map[string]int)
	m["theKey"] = 42
	This will do an error

	With make
	m := make(map[string]int)
	m["theKey"] = 42
	This will not do an error

	Memory is deallocated by garbage collection
		- Objects out of scope or set to nil are eligible
		- The GC will free the memory when it is no longer needed
		- We can use the keyword "defer" to free the memory at the end of the function
		- The garbage collector was updated in the version 1.5 of Go to be more performance
*/

/*
POINTERS

	Pointers are variables that contains the memory address of another variable

	anInt =: 42
	aPointer := &anInt -> This is a pointer to anInt

	To obtain the value we have to do
		- *aPointer -> This is the value of the pointer
		- aPointer -> This is the memory address of the value

	To declare the type pointer we use the keyword "*"
	anInt := 42
	var aPointer *int = &anInt

	If we change a value of a pointer we change the value of
	the variable that the pointer points to
*/

/*
STRUCTS

	We can create structs with the keyword "struct"
		- Is like a class in Java or Struct in C
		- Go doesn't have inheritance
		- Structs are independent of each other

	type Dog struct {
		Breed string
		Weight int
	}

	If we type the name with an UPPERCASE the struct will be available to all
	the go app
	If we do it with a lowercase the struct will be only available to the package

	To assing a variable to a struct

	var dog Dog = Dog{Breed: "Labrador", Weight: 30}

	We don't have the need to define a constructor, we just pass the value as parameters
	in the order as they are defined in the struct

	The exported structs, that is the ones that are written with UPPERCASE
	are available to all the packages, and need a comment above the definition
	to explain what the strcut is about

	We can encapsulate functionallity in form of methods in structs

	a Method is a member of a struct

	To attach a method to an struct we have to create a separte func

	func (d Dog) Speak() { -> When we do this we are creating a new copy of the struct Dog, that meaning if we change a value of the struct, this will not be reflajada in the original
		fmt.Println(d.Breed, "says", d.sound)
	}

	dog.Speak()

	To modify the original struct we have to use the keyword "pointer"

*/

/*
MAPS

	Is an unordered collection of key-value pairs (hash table) (dict) (associated arrays)

	We can use int, strings, etc as keys

	To initialize a map we use the keyword "make"

	states := make(map[string]string)

	We can retrieve items using the key

	states["CA"] = "California"

	To remove an item from the map we use the keyword "delete"

	delete(states, "CA")

	To add an item to the map we use

	states["NY"] = "New York"

	To loop through the map we use the keyword "range"

	for k, v := range states {
		println(k, v)
	}

	If we want to order the map we can make a slices of the keys
	and then sorted with the sort package

	keys := make([]string, len(states))])
	i := 0
	for k := range states {
		keys[i] = k
		i++
	}
	sort.Strings(keys)

	for i := range keys {
		fmt.Println(states[keys[i]])
	}

*/

/*
CONDITIONALS

	IF

	We can use if, else if, else, switch, and for
	the difference with other languages is that we don't have
	to use parenthesis to define the condition and another condition
	is that the open curly brace has to bee in the same line as the condition

	if condition {
		do something
	} else if condition {
		do something else
	} else {

	}

	We can initialize a variable with a condition

	if x:= -42; x < 0 {
		println(x)
	}

	SWITCH

	We can use switch to execute different actions depending on the value of a variable

	switch x {
		case 0:
			println("Zero")
		case 1:
			println("One")
		default:
			println("Unknown")
	}

	We can use the keyword "fallthrough" to execute the next case
	The "fallthrough" keyword makes the switch statement execute the next case

	switch x {
		case 0:
			println("Zero")
			fallthrough
		case 1:
			println("One")
		default:
			println("Unknown")

	and we can initialize a variable with a condition

	switch dow:= rand.Intn(7) + 1; dow {
		case 1:
			println("Monday")
		case 2:
			println("Tuesday")
		case 3:
			println("Wednesday")
		case 4:
			println("Thursday")
		case 5:
			println("Friday")
		case 6:
			println("Saturday")
		case 7:
			println("Sunday")
	}
*/

func main() {

	vars()

	userInput()

	convertStringToNumber()

	firstInitial, SecondInitial := getInitials("John Doe")

	fmt.Println(firstInitial, SecondInitial)

	pointer()

	maps()

	poodle := Dog{Breed: "Poodle", Weight: 10, Sound: "Woof"}

	fmt.Println(poodle)

	poodle.Speak()

	poodle.SpeakPointer()

	Labels()

	DeferKeyword()
}

func vars() {
	var aSring string = "Hello"

	fmt.Println(aSring)

	fmt.Printf("The variable type is %T\n", aSring)

	var defaultInt int = 10

	fmt.Println(defaultInt)

	name := "John"

	fmt.Println(name)
}

func userInput() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter your name: ")
	input, _ := reader.ReadString('\n')

	fmt.Println("Hello", input)
}

func convertStringToNumber() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter a number: ")
	numInput, _ := reader.ReadString('\n')
	aFloat, err := strconv.ParseFloat(strings.TrimSpace(numInput), 64)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(aFloat)
}

func getInitials(n string) (string, string) {
	n = strings.ToUpper(n)
	names := strings.Split(n, " ")

	var initials []string
	for _, value := range names {
		initials = append(initials, string(value[:1]))
	}

	if len(initials) == 1 {
		return initials[0], ""
	}

	return initials[0], initials[1]
}

func pointer() {
	var p *int // This is a pointer that don't point to anything
	fmt.Println("Value of p: ", p)
	anInt := 42
	var p2 = &anInt
	fmt.Println("Value of p: ", *p2)
}

func maps() {
	states := make(map[string]string)
	states["CA"] = "California"
	states["TX"] = "Texas"
	states["FL"] = "Florida"

	california := states["CA"]

	delete(states, "CA")

	states["NY"] = "New York"

	fmt.Println(states)
	fmt.Println(california)

	for k, v := range states {
		fmt.Println(k, v)
	}

	keys := make([]string, len(states))

	i := 0

	for k := range states {
		keys[i] = k
		i++
	}

	sort.Strings(keys)

	for i := range keys {
		fmt.Println(states[keys[i]])
	}
}

// Dog Struct
type Dog struct {
	Breed  string
	Weight int
	Sound  string
}

func (d Dog) Speak() {
	fmt.Println(d.Breed, " says ", d.Sound)
}

func (d *Dog) SpeakPointer() {
	d.Sound = "Arf"
}

func Labels() {
	var out int

	for j := 0; j < 20; j++ {
		out = j*j + out
		if out > 12 {
			goto theEnd
		}
	}

theEnd:
	fmt.Println(out)
}

func DeferKeyword() {
	resp, err := http.Get("http://www.google.com")

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	bytes, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		panic(err)
	}

	content := string(bytes)

	fmt.Println(content)
}
