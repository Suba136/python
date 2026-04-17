def main():
    user_name = input("Enter a name: ")
    user_age= int(input("Enter a age: "))
    days = user_age * 365
    print(f"Hello,{user_name}! You are appropriately {days}days old")

if __name__== "__main__":
    main()