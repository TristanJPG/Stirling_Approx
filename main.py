from math import pi, pow, factorial, e, sqrt

# N = input("What number do you want to test? ")

# Stirling Approximation - Instead of using the full factorial equation (N * N-1 -> N^0) you can get a close,
# but not exact estimate (Approx. ~) using the formula - √2πN * (N/e)^N.
N = 170
# Test 1 - The Factorial
product1 = factorial(N)
print(f"Factorial Method = {product1}")

print("------------------------------------------------")

# Test 2 - The Stirling Approach.
product2 = (sqrt(2*pi*N) * pow((N/e), N))

print(f"Stirling's Method = {int(product2)}")

# The ratio between the two products to see how close the ~ is.
print("------------------------------------------------")
ratio = product1/product2

if ratio == 1:
    print('Boom')
else:
    print(f"The ratio is {ratio}")

