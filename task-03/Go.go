package main

import (
	"fmt"
	"math"
)

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	if num <= 3 {
		return true
	}
	if num%2 == 0 || num%3 == 0 {
		return false
	}
	i := 5
	for i*i <= num {
		if num%i == 0 || num%(i+2) == 0 {
			return false
		}
		i += 6
	}
	return true
}

func findPrimesUpToN(n int) []int {
	primes := []int{}
	for num := 2; num <= n; num++ {
		if isPrime(num) {
			primes = append(primes, num)
		}
	}
	return primes
}

func main() {
	var n int
	fmt.Print("Enter a number (n): ")
	_, err := fmt.Scanf("%d", &n)

	if err != nil || n < 2 {
		fmt.Println("Invalid input. Please enter a valid number greater than or equal to 2.")
		return
	}

	primeNumbers := findPrimesUpToN(n)
	fmt.Printf("Prime numbers up to and including %d are: %v\n", n, primeNumbers)
}
