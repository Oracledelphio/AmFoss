function isPrime(num) {
    if (num <= 1) {
        return false;
    }
    if (num <= 3) {
        return true;
    }
    if (num % 2 === 0 || num % 3 === 0) {
        return false;
    }
    let i = 5;
    while (i * i <= num) {
        if (num % i === 0 || num % (i + 2) === 0) {
            return false;
        }
        i += 6;
    }
    return true;
}

function findPrimesUpToN(n) {
    const primes = [];
    for (let num = 2; num <= n; num++) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }
    return primes;
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter a number (n): ', (input) => {
    const n = parseInt(input);
    if (isNaN(n) || n < 2) {
        console.log('Invalid input. Please enter a valid number greater than or equal to 2.');
    } else {
        const primeNumbers = findPrimesUpToN(n);
        console.log(`Prime numbers up to and including ${n} are: ${primeNumbers.join(', ')}`);
    }
    rl.close();
});
