import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PrimeFinder {
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        if (num <= 3) {
            return true;
        }
        if (num % 2 == 0 || num % 3 == 0) {
            return false;
        }
        int i = 5;
        while (i * i <= num) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
        return true;
    }

    public static List<Integer> findPrimesUpToN(int n) {
        List<Integer> primes = new ArrayList<>();
        for (int num = 2; num <= n; num++) {
            if (isPrime(num)) {
                primes.add(num);
            }
        }
        return primes;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number (n): ");
        int n = scanner.nextInt();

        if (n < 2) {
            System.out.println("There are no prime numbers up to and including " + n);
        } else {
            List<Integer> primeNumbers = findPrimesUpToN(n);
            System.out.print("Prime numbers up to and including " + n + " are: ");
            for (int i = 0; i < primeNumbers.size(); i++) {
                System.out.print(primeNumbers.get(i));
                if (i < primeNumbers.size() - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println();
        }
        scanner.close();
    }
}
