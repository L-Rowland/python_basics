# Math Python Library

import math

# Exponents

# 4 to the power raised to 5

print(4**5) # 4 is base, 5 is power
print(2**2)
print(-2**3)

# Square Root

print(math.sqrt(16)) # sqrt = square root. 16 is the parameter. Function is located in math
print(math.sqrt(36))

# Power Function

print(math.pow(4,5)) # 4 is base, 5 is power. pow = power


# Exponential and Logarithm

print("Exponential of 2", math.exp(1))
# e^2

print("Natural log of 10:", math.log(10))
# log(10) or ln(10)
# log base is e, e = ~2.8

print("Log base 10 of 100:", math.log10(100))

# Absolute Value

print("Absolute value of -5:", math.fabs(-5))

#Factorial
print("factorial of 5:", math.factorial(5))

# Convert Radians to Degrees

angle = 45
radians = math.radians(angle)
print(radians)

# Angle must be converted to radians

# Sin Cos Tan

print("Sine of 45 degrees:", math.sin(radians))

print("Cos of 45 degrees:", math.cos(radians))

print("Tan of 45 degrees:", math.tan(radians))

angle = 60
radians = math.radians(angle)
print(radians)

print("Sine of 60 degrees:", math.sin(radians))

print("Cos of 60 degrees:", math.cos(radians))

print("Tan of 60 degrees:", math.tan(radians))

# Inverse Trigonometry

print("Arcsin of 60 degrees:", math.asin(0.8660254037844386))

print("Arccos of 60 degrees:", math.acos(0.5000000000000001))

print("Arctan of 60 degrees:", math.atan(1.7320508075688767))

print("Arcsin of 60 degrees:", math.degrees(math.asin(0.8660254037844386)))

print("Arccos of 60 degrees:", math.degrees(math.acos(0.5000000000000001)))

print("Arctan of 60 degrees:", math.degrees(math.atan(1.7320508075688767)))

# Mathmatical Constants: Values that have no end

print("Value of Pi:", math.pi)

print("Value of e:", math.e)

print("value of tau:", math.tau)

print("Infinity:", math.inf)

print("Not-a-number (NaN):", math.nan)