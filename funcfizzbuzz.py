def fizzbuzz(n):
    r=n
    if n%3 == 0:
        r="Fizz"
    if n%5 == 0:
        r="Buzz"
    if n%5 == 0 and n%3 == 0:
        r="FizzBuzz"
    return r
