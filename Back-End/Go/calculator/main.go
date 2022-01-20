package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calculator() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Enter a value:")
	firstInput, _ := reader.ReadString('\n')
	firstNumInput, firstInputErr := strconv.ParseFloat(strings.TrimSpace(firstInput), 64)

	fmt.Println("Enter a second value:")
	secondInput, _ := reader.ReadString('\n')
	secondNumInput, secondInputErr := strconv.ParseFloat(strings.TrimSpace(secondInput), 64)

	if firstInputErr != nil || secondInputErr != nil {
		println("Error: ", firstInputErr, secondInputErr)
	}

	println("Wich operation do you want to perform?")
	operation, _ := reader.ReadString('\n')

	switch strings.TrimSpace(operation) {
	case "+":
		fmt.Println("The result is: ", firstNumInput+secondNumInput)
	case "-":
		fmt.Println("The result is: ", firstNumInput-secondNumInput)
	case "*":
		fmt.Println("The result is: ", firstNumInput*secondNumInput)
	case "/":
		fmt.Println("The result is: ", firstNumInput/secondNumInput)
	default:
		fmt.Println("Invalid operation")
	}

}

func main() {
	calculator()
}
