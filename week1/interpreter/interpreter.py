def main():
    x,y,z = input("Expression: ").split()
    print(f"{interpreter(x,y,z):.1f}")

def interpreter(x,y,z):
    x, z = float(x), float(z)   
    return x + z if y == "+" else x - z if y == "-" else x / z if y == "/" else x * z
    

if __name__ == "__main__":
    main()