def main():
    time = input("What time is it? ")
    print(convert(time))


def convert(time):
    hours, minutes = time.split(":")
    time = int(hours) + int(minutes)/60
    return "breakfast" if 7 <= time <= 8 else "lunch" if 12 <= time <= 13 else "dinner" if 18 <= time <= 19 else ""


if __name__ == "__main__":
    main()