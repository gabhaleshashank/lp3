# Fibonacci Numbers - Iterative, Naïve Recursive, and Optimized Recursive (Memoization)
# Includes Time & Space Complexity for each method
# -------------------------------
# Non-Recursive Fibonacci (Iterative)
# Time Complexity: O(n)  -> Loop runs (n-2) times
# Space Complexity: O(n) -> Stores entire sequence (O(1) if storing only last 2 numbers)
def fibonacci_non_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq
# -------------------------------
# Recursive Fibonacci (Naïve)
# Time Complexity: O(2^n) -> Each call branches into 2 more calls
# Space Complexity: O(n)  -> Function call stack depth up to n
def fibonacci_recursive_naive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_naive(n - 1) + fibonacci_recursive_naive(n - 2)
# -------------------------------
# Optimized Recursive Fibonacci (Memoization)
# Time Complexity: O(n)  -> Each number computed once, stored in cache
# Space Complexity: O(n) -> Cache + recursion stack depth
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive_memo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_memo(n - 1) + fibonacci_recursive_memo(n - 2)
# -------------------------------
# Input from user
n = int(input("Enter the number of terms in Fibonacci sequence: "))

# Results
print("\nIterative Fibonacci sequence:", fibonacci_non_recursive(n))
print("Naïve Recursive Fibonacci sequence:", [fibonacci_recursive_naive(i) for i in range(n)])
print("Optimized Recursive (Memoized) Fibonacci sequence:", [fibonacci_recursive_memo(i) for i in range(n)])
