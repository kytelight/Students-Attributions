import sys
from StudentsAttributions import Actions, Class, Allocations, DataHandler

# Check for right usage:
#   - approach = rule-engine
#   - approach = if-statements
if len(sys.argv) != 2:
    sys.exit("Usage: python main.py approach")


# Define rules

rules = {
    # Rainbow High
    "school == 'Rainbow High'": [
        "IQ > 116",
        "IQ < 90",
        "age > 18",
        "sex == 'Male' and assiduity_score <= 2",
        "sex == 'Female' and assiduity_score <= 2",
        "true",
    ],

    # Waterfalls School for Girls 
    "school == 'Waterfalls School for Girls'": [
        "IQ > 116",
        "IQ < 90",
        "age < 18",
        "assiduity_score >= 4",
        "assiduity_score <= 2",
        "true",
    ],

    # Cape Coral High
    "school == 'Cape Coral High'": [
        "age < 18 and IQ > 116 and nationality == 'Home'",
        "age < 18 and IQ > 116 and nationality == 'International'",
        "age > 18 and IQ < 90",
        "assiduity_score >= 4",
        "assiduity_score <= 2",
        "true"
    ],
}

# Input/output locations
load_path = "<students_dataset>"
save_path = "<allocated_students_save_path>.csv"

# DataHandler
handler = DataHandler(load_path)
students = handler.load_students()

if (sys.argv[1] == "rule-engine"):

    actions =  Actions(
        logic = {
            0: Class("A"),
            1: Class("B"),
            2: Class("C"),
            3: Class("D"),
            4: Class("E"),
            5: Class("F") 
        }
    )

    # Allocate students using rule engine
    alloc1 = Allocations({})
    allocations1 = alloc1.allocate_students_rule_engine(actions, rules, students)

    # Save allocated students
    handler.save_students(load_path, save_path, allocations1)

elif (sys.argv[1] == "if-statements"):

    # Allocate students using if else statements
    alloc2 = Allocations({})
    allocations2 = alloc2.allocate_students_if_statements(rules, students)

    # Save allocated students
    handler.save_students(load_path, save_path, allocations2)

else:
    sys.exit("Incorrect arguments. Did you mean: rule-engine or if-statements?")
