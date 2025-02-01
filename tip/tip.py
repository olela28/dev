def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(f"Leave ${dollars * percent:.2f}")


def dollars_to_float(convert):
    return  float(convert.removeprefix("$"))


def percent_to_float(changed):
    return float(changed.removesuffix("%")) / 100
    

main()
