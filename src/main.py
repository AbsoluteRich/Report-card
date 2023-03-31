scales = ["original", "omni", "omni_simple"]


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
            if percent >= 90:
                return "A"
            elif percent >= 80:
                return "B"
            elif percent >= 70:
                return "C"
            elif percent >= 60:
                return "D"
            else:
                return "F"  # Sometimes E is used in place of F


if __name__ == "__main__":
    import json
    from rich import table, print as rprint

    # Loads the file
    with open("grades.json", "r") as f:
        input_grades = json.loads(f.read())
    del f

    # Gets the grade scale
    # Your results will vary wildly depending on which one you use, so it's always good to ask
    rprint("Choose a grading scale")
    rprint(f"Your choices: {scales}")
    input_scale = input("").casefold()
    
    if input_scale not in scales:
        input_scale = "original"

    # Generates the letter grades
    letter_grades = {}
    for x in input_grades:
        letter_grades[x] = calculate_lgrade(input_grades[x], input_scale)

    # Creates a Rich table to store the data
    table = table.Table(title="Report card")

    table.add_column("Subject")
    table.add_column("Grade")

    for y in letter_grades:
        table.add_row(y, letter_grades[y])

    # Finally, outputs the information to both the screen and a file
    rprint(table)

    with open("output.txt", "w") as f:
        rprint(table, file=f)
