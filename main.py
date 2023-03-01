"""
*** Report card app ***
Takes in a dictionary or JSON file of subjects and percent grades, returns the letter grade associated with it
Uses Rich to put the information into a table and make it look pretty
"""


# Greater than or equal to 75       A
# Greater than or equal to 60       B
# Greater than or equal to 35       C
# Less than 35                      D


def calculate_lgrade(percent, grade_scale="original"):
    match grade_scale:
        case "original":
            if percent >= 75:
                return "A"
            elif percent >= 60:
                return "B"
            elif percent >= 35:
                return "C"
            elif percent < 35:
                return "D"

        case "omni":  # https://www.omnicalculator.com/other/grade#how-this-grading-calculator-works
            if percent >= 97:
                return "A+"
            elif percent >= 93:
                return "A"
            elif percent >= 90:
                return "A-"
            elif percent >= 87:
                return "B+"
            elif percent >= 83:
                return "B"
            elif percent >= 80:
                return "B-"
            elif percent >= 77:
                return "C+"
            elif percent >= 73:
                return "C"
            elif percent >= 70:
                return "C-"
            elif percent >= 67:
                return "D+"
            elif percent >= 63:
                return "D"
            elif percent >= 60:
                return "D-"
            else:
                return "F"

        case "omni_simple":
            pass


if __name__ == "__main__":
    import json
    from rich import table, print as rprint

    # Loads the file
    with open("grades.json", "r") as f:
        input_grades = json.loads(f.read())
    del f

    # Gets the grade scale
    input_scale = input("Choose grading scale: ").casefold()
    if input_scale not in ["original", "omni"]:
        input_scale = "original"

    # Generates the letter grades
    letter_grades = {}
    for x in input_grades:
        letter_grades[x] = calculate_lgrade(input_grades[x], input_scale)

    # Outputs it in a table using Rich
    table = table.Table(title="Report card")

    table.add_column("Subject")
    table.add_column("Grade")

    for y in letter_grades:
        table.add_row(y, letter_grades[y])

    with open("output.txt", "w") as f:
        rprint(table, file=f)

