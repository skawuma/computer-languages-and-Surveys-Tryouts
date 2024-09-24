package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)


//tribonacci calculates the tribonacci series of numbers n returned in an array.
// It returns an array representing tribonacci  series  of n number of integer Value
func tribonacci(n int) []int {
    // Base cases
	if n <= 0 {
		return []int{}
	} else if n == 1 {
		return []int{0}
	} else if n == 2 {
		return []int{0, 1}
	} else {
		// Initialize the first three Tribonacci numbers
		fibSeq := []int{1, 1, 1}
		for i := 3; i < n; i++ {
			// Calculate the current Tribonacci number
			nextNum := fibSeq[i-1] + fibSeq[i-2] + fibSeq[i-3]
			// Update the last three Tribonacci numbers
			fibSeq = append(fibSeq, nextNum)
		}
		// Return the nth Tribonacci number
		return fibSeq
	}
}

func main() {
	//fmt.Println(tribonacci(20))

	scanner := bufio.NewScanner(os.Stdin)

	for {

		fmt.Print("Enter a positive integer: ")
		scanner.Scan()
		input := strings.TrimSpace(scanner.Text())

		number, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println("Invalid input. Please enter an integer.")
			continue
		}

		if number < 0 {
			fmt.Println("Number must be positive.")
			continue
		}

		fmt.Println(tribonacci(20))
		 // Ask user to  Exit loop if input is valid
		var userInput string
		fmt.Print("Do you want to continue (type 'y' to continue and 'n' to quit): ")
		fmt.Scanln(&userInput)
		if userInput == "y" {
			continue
		} else if userInput == "n" {
			fmt.Println("Program Exiting....")
			break
		}

	}
}
