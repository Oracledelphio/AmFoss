#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int num)
{
    if (num <= 1)
    {
        return false;
    }
    if (num <= 3)
    {
        return true;
    }
    if (num % 2 == 0 || num % 3 == 0)
    {
        return false;
    }
    int i = 5;
    while (i * i <= num)
    {
        if (num % i == 0 || num % (i + 2) == 0)
        {
            return false;
        }
        i += 6;
    }
    return true;
}

void findPrimesUpToN(int n)
{
    printf("Prime numbers up to and including %d are: ", n);
    for (int num = 2; num <= n; num++)
    {
        if (isPrime(num))
        {
            printf("%d ", num);
        }
    }
    printf("\n");
}

int main()
{
    int n;
    printf("Enter a number (n): ");
    scanf("%d", &n);

    if (n < 2)
    {
        printf("There are no prime numbers up to and including %d\n", n);
    }
    else
    {
        findPrimesUpToN(n);
    }

    return 0;
}