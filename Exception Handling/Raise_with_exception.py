def check_age(age):
    if age < 18:
        raise ValueError("You must be an adult to enter this site.")
    else:
        print("Enjoy.")

try:
    check_age(int(input("Enter your age: ")))
except ValueError as e:
    print("Access denied: ", e)