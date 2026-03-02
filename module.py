# two_sum takes two integer arguments and returns the sum of the integers
def two_sum(a: int, b: int) -> int:    
  Result =  a + b 
  return Result 

# remove_vowels takes a string argument and return a string with all vowels removed
def remove_vowels(s: str) -> str:
  vowels = ["a", "e" , "i", "o", "u"]
  string = ""
  for char in s:
     if char not in  vowels:
        string = string + char
  return string

# factorial takes an integer argument and returns the factorial result of that integer
# factorial must use iteration and not the built-in factorial function
def factorial(num: int) -> int:
    pass

# listify takes a string argument and returns a list of characters in the string
def listify(s: str) -> list:
    pass