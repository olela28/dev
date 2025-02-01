snake_case = []
for c in input("camelCase: "):
    if c.isupper():
        snake_case.append("_")
        snake_case.append(c.lower())
    else:
        snake_case.append(c)
print(f"snake_case: {"".join(snake_case)}")
        