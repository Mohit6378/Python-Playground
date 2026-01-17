num = ["10", "0", "abc", "5.2", "2"]

for n in num:
    try:
        print("Result: ", (10 / int(n)))
    except Exception as e:
        print("error with", n, ": ", e)