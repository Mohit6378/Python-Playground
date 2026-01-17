import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:
    logging.error("Error occurred: %s", e)
    print("Error logged to file.")