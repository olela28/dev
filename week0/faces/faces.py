def main():
    emoticon = input("Enter your input here: ")
    print(convert(emoticon))
    

def convert(to):
    return to.replace(":)", "🙂").replace(":(", "🙁")


main()