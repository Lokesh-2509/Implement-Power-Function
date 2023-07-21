def pow_modulo(A, B, C):
    if B == 0:
        return 1 % C
    result = pow_modulo(A, B // 2, C)
    result = (result * result) % C

    if B % 2 == 1:
        result = (result * A) % C

    return result
if __name__ == "__main__":
    try:
        A = int(input("Enter the value of A: "))
        B = int(input("Enter the value of B: "))
        C = int(input("Enter the value of C: "))
        if A < 0 or B < 0 or C <= 0:
            print("Please enter non-negative values for A and B, and a positive value for C.")
        else:
            result = pow_modulo(A, B, C)
            print(f"The result of ({A}^{B} % {C}) is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid non-negative integers for A, B, and a positive integer for C.")
