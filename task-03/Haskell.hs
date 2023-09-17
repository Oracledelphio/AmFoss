import Data.List (nub)

isPrime :: Int -> Bool
isPrime n
    | n <= 1    = False
    | n <= 3    = True
    | otherwise = all (\x -> n `mod` x /= 0) [2..intSqrt n]

intSqrt :: Int -> Int
intSqrt = floor . sqrt . fromIntegral

findPrimesUpToN :: Int -> [Int]
findPrimesUpToN n = nub [x | x <- [2..n], isPrime x]

main :: IO ()
main = do
    putStrLn "Enter a number (n):"
    input <- getLine
    let n = read input :: Int

    if n < 2
        then putStrLn "There are no prime numbers up to and including the input number."
        else do
            let primeNumbers = findPrimesUpToN n
            putStrLn $ "Prime numbers up to and including " ++ show n ++ " are: " ++ show primeNumbers
