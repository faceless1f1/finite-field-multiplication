# 2^n Galois Field Multiplication Calculator

## Usage
- **A:** the first input to calculator
- **B:** the second input to calculator
- **Polynomial:** the irreducible polynomial of the field
- **Degree:** the degree of the field

## Features
- Automatically reduce input elements to canonical field elements
- Solve Galois Field Multiplication iteratively
- Shows full output so the user can follow along

## Example Output
```yaml
A (in decimal): 24
B (in decimal): 64
Polynomial (e.g., x^3+x+1): x^3+x+1
Degree (in decimal): 3

>>> Reducing input a:

--- Reduction Process Start ---
Current polynomial: x^4+x^3  (binary: 11000)
  Degree = 4; needs degree < 3
  Shifting irreducible poly by 1:
    Irreducible poly shifted: x^4+x^2+x  (binary: 10110)
  After XOR, new value: x^3+x^2+x  (binary: 1110)
Current polynomial: x^3+x^2+x  (binary: 1110)
  Degree = 3; needs degree < 3
  Shifting irreducible poly by 0:
    Irreducible poly shifted: x^3+x+1  (binary: 1011)
  After XOR, new value: x^2+1  (binary: 101)
--- Reduction Process End ---

>>> Reducing input b:

--- Reduction Process Start ---
Current polynomial: x^6  (binary: 1000000)
  Degree = 6; needs degree < 3
  Shifting irreducible poly by 3:
    Irreducible poly shifted: x^6+x^4+x^3  (binary: 1011000)
  After XOR, new value: x^4+x^3  (binary: 11000)
Current polynomial: x^4+x^3  (binary: 11000)
  Degree = 4; needs degree < 3
  Shifting irreducible poly by 1:
    Irreducible poly shifted: x^4+x^2+x  (binary: 10110)
  After XOR, new value: x^3+x^2+x  (binary: 1110)
Current polynomial: x^3+x^2+x  (binary: 1110)
  Degree = 3; needs degree < 3
  Shifting irreducible poly by 0:
    Irreducible poly shifted: x^3+x+1  (binary: 1011)
  After XOR, new value: x^2+1  (binary: 101)
--- Reduction Process End ---

>>> After Reduction:
  a (original 24) reduced to 5 -> x^2+1
  b (original 64) reduced to 5 -> x^2+1


=== Multiplication Process Start ===

----------------------------------------
Initial a = 5 -> x^2+1 (binary: 0101)
Initial b = 5 -> x^2+1 (binary: 0101)
Initial result = 0 -> 0 (binary: 0000)
----------------------------------------

----------------------------------------
Iteration 1:
  b LSB is 1: XOR result with a
    0 XOR x^2+1 -> x^2+1
  Shift b right: x^2+1 -> x (binary: 0010)
  Shift a left: x^2+1 -> x^3+x (binary: 1010) -> overflow detected, reduced to 1 (binary: 0001)
----------------------------------------
Iteration 2:
  b LSB is 0: result unchanged
  Shift b right: x -> 1 (binary: 0001)
  Shift a left: 1 -> x (binary: 0010) (no overflow)
----------------------------------------
Iteration 3:
  b LSB is 1: XOR result with a
    x^2+1 XOR x -> x^2+x+1
  Shift b right: 1 -> 0 (binary: 0000)
  Shift a left: x -> x^2 (binary: 0100) (no overflow)
----------------------------------------

=== Multiplication Process End ===

24 times 64 in the finite field of 2 to the power of 3 over x^3+x+1: 7 -> polynomial form = x^2+x+1
```
