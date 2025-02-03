user_input = []
for c in input("Input: ").lower():
   match c:
      case "a" | "e" | "i" | "o" | "u":
         user_input.append(c.replace("a","").replace("e","").replace("i","").replace("o","").replace("u",""))
      case _:
         user_input.append(c)
print("".join(user_input))

