defmodule PrimeFinder do
  def is_prime(1), do: false
  def is_prime(n) when n > 1, do: is_prime(n, 2)

  defp is_prime(n, divisor) when divisor * divisor > n, do: true
  defp is_prime(n, divisor) when rem(n, divisor) == 0, do: false
  defp is_prime(n, divisor), do: is_prime(n, divisor + 1)
end

defmodule Main do
  def run do
    IO.puts("Enter a number (n): ")
    input = IO.gets("") |> String.trim()
    
    case String.to_integer(input) do
      {:ok, n} when n >= 2 ->
        primes = Enum.filter(2..n, &PrimeFinder.is_prime/1)
        IO.puts("Prime numbers up to and including #{n} are: #{Enum.join(primes, ", ")}")
      _ ->
        IO.puts("Invalid input. Please enter a valid number.")
    end
  end
end

Main.run()
