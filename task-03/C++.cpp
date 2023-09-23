#include <iostream>
#include <vector>

using namespace std;

// Function to find all prime numbers up to and including n
void findPrimes(int n)
{
    vector<bool> isPrime(n + 1, true);

    for (int p = 2; p * p <= n; ++p)
    {
        if (isPrime[p])
        {
            for (int i = p * p; i <= n; i += p)
            {
                isPrime[i] = false;
            }
        }
    }

    cout << "Prime numbers up to " << n << " are:" << endl;
    for (int i = 2; i <= n; ++i)
    {
        if (isPrime[i])
        {
            cout << i << " ";
        }
    }
    cout << endl;
}

int main()
{
    int n;

    cout << "Enter a number n: ";
    cin >> n;

    if (n < 2)
    {
        cout << "There are no prime numbers less than 2." << endl;
    }
    else
    {
        findPrimes(n);
    }

    return 0;
}
