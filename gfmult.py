def int_to_poly(num):
    """Converts an integer to a polynomial string (e.g. 11 -> x^3+x+1)."""
    if num == 0:
        return "0"
    
    terms = []
    power = 0
    while num > 0:
        if num & 1:
            if power == 0:
                terms.append("1")
            elif power == 1:
                terms.append("x")
            else:
                terms.append(f"x^{power}")
        num = num >> 1
        power += 1
    return "+".join(terms[::-1])


def poly_string_to_int(poly_str):
    """Converts a polynomial string into its integer representation."""
    poly_str = poly_str.replace(" ", "")
    terms = poly_str.split('+')
    result = 0
    for term in terms:
        if term == "1":
            exp = 0
        elif term == "x":
            exp = 1
        elif term.startswith("x^"):
            try:
                exp = int(term[2:])
            except ValueError:
                raise ValueError(f"Invalid exponent in term: {term}")
        else:
            raise ValueError(f"Unrecognized term: {term}")
        result |= (1 << exp)
    return result


def gf_reduction(num, polynomial, n):
    """
    Reduces the integer 'num' (representing a polynomial over GF(2))
    modulo the irreducible 'polynomial' defining GF(2^n). Outputs simplified,
    step-by-step details of the reduction process.
    """
    print("\n--- Reduction Process Start ---")
    while num.bit_length() - 1 >= n:
        current_deg = num.bit_length() - 1
        shift = current_deg - n
        print(f"Current polynomial: {int_to_poly(num)}  (binary: {num:b})")
        print(f"  Degree = {current_deg}; needs degree < {n}")
        poly_shifted = polynomial << shift
        print(f"  Shifting irreducible poly by {shift}:")
        print(f"    Irreducible poly shifted: {int_to_poly(poly_shifted)}  (binary: {poly_shifted:b})")
        num ^= poly_shifted
        print(f"  After XOR, new value: {int_to_poly(num)}  (binary: {num:b})")
    print("--- Reduction Process End ---\n")
    return num


def gf_multiply(a, b, polynomial, n):
    """
    Multiplies two elements in GF(2^n) using the shift-and-add (XOR) method.
    Assumes a and b are already reduced (canonical).
    """
    result = 0
    iteration = 1
    print("\n=== Multiplication Process Start ===")
    print("\n" + (("-") * 40))
    print(f"Initial a = {a} -> {int_to_poly(a)} (binary: {a:0{n+1}b})")
    print(f"Initial b = {b} -> {int_to_poly(b)} (binary: {b:0{n+1}b})")
    print(f"Initial result = {result} -> {int_to_poly(result)} (binary: {result:0{n+1}b})")
    print("-" * 40)

    if b:
        print("\n" + "-" * 40)

    while b:
        print(f"Iteration {iteration}:")
        if b & 1:
            print(f"  b LSB is 1: XOR result with a")
            old_result = result
            result ^= a
            print(f"    {int_to_poly(old_result)} XOR {int_to_poly(a)} -> {int_to_poly(result)}")
        else:
            print("  b LSB is 0: result unchanged")
        
        old_b = b
        b >>= 1
        print(f"  Shift b right: {int_to_poly(old_b)} -> {int_to_poly(b)} (binary: {b:0{n+1}b})")
        
        old_a = a
        a <<= 1
        print(f"  Shift a left: {int_to_poly(old_a)} -> {int_to_poly(a)} (binary: {a:0{n+1}b})", end="")
        # Check for overflow: if a has bit in position 2^n, reduce modulo polynomial
        if a & (1 << n):
            print(" -> overflow detected", end="")
            a ^= polynomial
            print(f", reduced to {int_to_poly(a)} (binary: {a:0{n+1}b})")
        else:
            print(" (no overflow)")
        
        print("-" * 40)
        iteration += 1

    print("\n=== Multiplication Process End ===")
    return result


def gf_reduce_inputs(a, b, polynomial, n):
    print("\n>>> Reducing input a:")
    a_reduced = gf_reduction(a, polynomial, n)
    print(">>> Reducing input b:")
    b_reduced = gf_reduction(b, polynomial, n)
    
    print(">>> After Reduction:")
    print(f"  a (original {a}) reduced to {a_reduced} -> {int_to_poly(a_reduced)}")
    print(f"  b (original {b}) reduced to {b_reduced} -> {int_to_poly(b_reduced)}\n")
    
    return gf_multiply(a_reduced, b_reduced, polynomial, n)


def main():
    a = int(input("\nA (in decimal): "))
    b = int(input("B (in decimal): "))
    poly_str = input("Polynomial (e.g., x^3+x+1): ")
    n = int(input("Degree (in decimal): "))
    
    polynomial = poly_string_to_int(poly_str)
    result = gf_reduce_inputs(a, b, polynomial, n)
    print(f"\n{a} times {b} in the finite field of 2 to the power of {n} over {int_to_poly(polynomial)}: {result} -> polynomial form = {int_to_poly(result)}\n\n")


if __name__ == "__main__":
    main()
