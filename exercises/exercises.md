# Sample Exercises (without solution)

Try to solve the exercises on your own and discuss in class your solution.


## A. Computational Complexity

### Exercise 1
Answer whether the following relations hold. Explain your answer:

- f(n) = Θ(g(n)) ⇒ f(n) = O(g(n))?
- f(n) = Θ(g(n)) ∧ g(n) = O(h(n)) ⇒ f(n) = O(h(n))
- f(n) = O(g(n)) ∧ g(n) = Θ(h(n)) ⇒ f(n) = O(h(n))
- n log(n) + Θ(sqrt(n)) = O(n sqrt(n))
- n^2 + 10n + 100 = O(n log(n))
- n^2 + (1.5)^n= O(2^(n/2))

### Exercise 2

Write an algorithm called Find-Largest that finds the largest number in an array using a *divide-and-conquer* strategy. 

What is the time complexity of your algorithm in terms of big-oh notation? Briefly justify your complexity analysis.

## B. Basic Data Structures

### Exercise 1. 
Consider the array:

    A = (29, 18, 10, 15, 20, 9, 5, 13, 2, 4, 15)
    
Does `A` satisfy the max-heap property? If not, fix it by swapping elements

Illustrate the execution of the heap-extract-max algorithm, which extracts the max element and then rearranges the array to satisfy the max-heap property.For each iteration or recursion of the algorithm, write the content of the array `A`.

### Exercise 2.

Implement an algorithm that checks whether a given expression `e` that contains parentheses (i.e., `(`, `)`, `{`, `}`, `[` and `]`) is balanced, i.e., for each open parenthesis there's a matching closing parenthesis and the order of opening and closing is respected.

Write sample unit tests to check that your program is correct. 

Unit tests have the form `T(e) = TRUE|FALSE` where `e` is the input expression and `TRUE|FALSE` is the expected value (`TRUE` means e is balanced).

#### Examples

The expression `a + b` is balanced, since it does not have any parenthesis. The corresponding unit test is: `T("a + b") = TRUE`.

The expression `{[]}` is also balanced, so `T{[]} = TRUE`.

However, the expressions `{[}]` and `{[}` are not balanced.

## C. Sorting

### Exercise 1. 

Illustrate the execution of the merge-sort algorithm on the array:

    A = (3,13,89,34,21,44,99,56,9)
    
For each fundamental iteration or recursion of the algorithm, write the content of the array. 

Assume the algorithm performs an in-place sort.

### Exercise 2.

Illustrate the execution of the radix sort algorithm on the array:

    A = (3,1113,2189,234,521,944,99,156,29)
    
For each fundamental iteration or recursion of the algorithm, write the content of the array. 

Assume the algorithm uses a stable sorting algorithm

## Searching

### Exercise 1.

Given the following array

    A = (3,13,89,34,21,44,99,56,9)
    
Illustrate the application of binary search to find the following elements:

- 71
- 9
- 56

### Exercise 2.

What is the time complexity of the binary search?