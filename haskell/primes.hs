import Data.List ((\\))

primesTo m = sieve [2..m]       {- (\\) is set-difference for unordered lists -}
             where 
             sieve (x:xs) = x : sieve (xs Data.List.\\ [x,x+x..m])
             sieve [] = []


main = do
    let a = primesTo 100000
    putStrLn "hello"
