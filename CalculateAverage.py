

def calculate_grade(numeric_grade):
    if 30 <= numeric_grade < 40:
        return "F"
    elif 40 <= numeric_grade < 50:
        return "E"
    elif 50 <= numeric_grade < 60:
        return "D"
    elif 60 <= numeric_grade < 70:
        return "C"
    elif 70 <= numeric_grade < 80:
        return "B"
    else:
        return "A"


def main():
    list_of_names = ["Aksh", "John", "Kevin", "Foster", "Jason", "Nelson", "Kenneth"]
    list_of_grades = [30, 87, 65, 78, 91, 100, 80]
    list_of_failures = []
    list_of_passers = []
    length_of_list = len(list_of_names)
    for i in range(length_of_list):
        grade = calculate_grade(list_of_grades[i])
        if grade == "F" or grade == "E":
            list_of_failures.append(list_of_names[i])
        else:
            list_of_passers.append(list_of_names[i])
        print(list_of_names[i] + " got a " + grade + " grade")
    print("\n")

    print("The following people PASSED!")
    for student in list_of_passers:
        print(student)
    print("\n")
    print("The following people failed :(")
    for student in list_of_failures:
        print(student)

main()