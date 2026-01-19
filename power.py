import sys
if len(sys.argv) != 3:
    print("Usage: python power.py <base> <exponent>")
    sys.exit(1)

base = int(sys.argv[1])
exponent = int(sys.argv[2])

if exponent < 0:
    print("Please provide a positive exponent value.")
    sys.exit(1)

result = base ** exponent

print(f"{base} raised to the power {exponent} is: {result}")
