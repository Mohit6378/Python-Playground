def calculate_percentage(marks_dict):
    total_marks = sum(float(marks) for marks in marks_dict.values())
    num_subjects = len(marks_dict)
    percentage = (total_marks / (num_subjects * 100)) * 100
    return percentage


marks = input("Enter subjects marks separated by commas:")
my_dict = dict(item.split(":") for item in marks.split(","))
result = calculate_percentage(my_dict)
print(f"percentage: {result}")