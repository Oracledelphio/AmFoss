def is_prime(num)
    return false if num <= 1
    return true if num <= 3
    return false if (num % 2 == 0) || (num % 3 == 0)
    i = 5
    while i * i <= num
      return false if (num % i == 0) || (num % (i + 2) == 0)
      i += 6
    end
    true
  end
  
  begin
    print "Enter a number (n): "
    n = gets.chomp.to_i
  
    if n < 2
      puts "There are no prime numbers up to and including #{n}"
    else
      primes = (2..n).select { |num| is_prime(num) }
      puts "Prime numbers up to and including #{n} are: #{primes.join(', ')}"
    end
  rescue ArgumentError
    puts "Invalid input. Please enter a valid number."
  end
  