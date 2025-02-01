x,y,z = input("Expression: ").split(" ")
x, z = float(x), float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "/":
    result = x / z
else:
    result = x * z

print(f"{result:.1f}")