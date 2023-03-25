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
load_path = "<students dataset>"
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


        
        
          


































#with open(load_path, mode= "r") as students:
            
#    reader = csv.DictReader(students)
#    for row in reader:
        #Cape Coral High

        #Rule 1: Male/Female of age < 18 and IQ > 116 and Home -> Class A
        #Rule 2: Male/Female of age < 18 and IQ > 116 and International -> Class B
        #Rule 3: Male/Female of age > 18 with IQ < 90  -> Class C
        #Rule 4: Male/Female with assiduity score >= 4 -> Class D
        #Rule 5: Male/Female with assiduity score <= 2 -> Class E 
        #Rule 6: rest  -> Class F

        #"age < 18 and IQ > 116 and nationality == 'Home'",
        #"age < 18 and IQ > 116 and nationality == 'International'",
        #"age > 18 and IQ < 90",
        #"assiduity_score >= 4",
        #"assiduity_score <= 2",
        #"true"

        #if (row["school"] == 'Cape Coral High'):

        #        if (int(row["age"]) < 18 and int(row["IQ"]) > 116 and row["nationality"] == "Home"):
        #            print("rule1" + "->" + row["ID"] + row["name"] + "->" + "Class A")

        #        elif (int(row["age"]) < 18 and int(row["IQ"]) > 116 and row["nationality"] == "International"):
        #            print("rule2" + "->" + row["ID"] + row["name"] + "->" + "Class B")

        #        elif (int(row["age"]) > 18 and int(row["IQ"]) < 90):
        #            print("rule3" + "->" + row["ID"] + row["name"] + "->" + "Class C")

        #        elif (int(row["assiduity_score"]) >= 4):
        #            print("rule4" + "->" + row["ID"] + row["name"] + "->" + "Class D")

        #        elif (int(row["assiduity_score"]) <= 2):
        #            print("rule4" + "->" + row["ID"] + row["name"] + "->" + "Class E")

        #        else:
        #            print("rule6" + "->" + row["ID"] + row["name"] + "->" + "Class F")

#        # IQ > 116",
#        # IQ < 90",
#        # age < 18",
#        #"assiduity_score >= 4",
#        #"assiduity_score <= 2",
#        #"true",

        #if (row["school"] == 'Waterfalls School for Girls'):

        #    if (int(row["IQ"]) > 116):
        #        print("rule1" + "->" + row["ID"] + row["name"] + "->" + "Class A")

        #    elif (int(row["IQ"]) < 90):
        #        print("rule2" + "->" + row["ID"] + row["name"] + "->" + "Class B")

        #    elif (int(row["age"]) < 18):
        #        print("rule3" + "->" + row["ID"] + row["name"] + "->" + "Class C")

        #    elif (int(row["assiduity_score"]) >= 4):
        #        print("rule4" + "->" + row["ID"] + row["name"] + "->" + "Class D")

        #    elif (int(row["assiduity_score"]) <= 2):
        #        print("rule4" + "->" + row["ID"] + row["name"] + "->" + "Class E")

        #    else:
        #        print("rule6" + "->" + row["ID"] + row["name"] + "->" + "Class F")


#        #"IQ > 116",
#        #"IQ < 90",
#        #"age > 18",
#        #"sex == 'Male' and assiduity_score <= 2",
#        #"sex == 'Female' and assiduity_score <= 2",
#        #"true",

        #if (row["school"] == 'Rainbow High'):

        #    if (int(row["IQ"]) > 116):
        #        print("rule1" + "->" + row["ID"] + row["name"] + "->" + "Class A")

        #    elif (int(row["IQ"]) < 90):
        #        print("rule2" + "->" + row["ID"] + row["name"] + "->" + "Class B")

        #    elif (int(row["age"]) > 18):
        #        print("rule3" + "->" + row["ID"] + row["name"] + "->" + "Class C")

        #    elif (str(row["sex"]) == "Male" and int(row["assiduity_score"]) <= 2):
        #        print("rule4" + "->" + row["ID"] + row["name"] + "->" + "Class D")

        #    elif (str(row["sex"]) == "Female" and int(row["assiduity_score"]) <= 2):
        #        print("rule4" + "->" + row["ID"] + row["name"] + "->" + "Class E")

        #    else:
        #        print("rule6" + "->" + row["ID"] + row["name"] + "->" + "Class F")






#Attr = Allocations("A", "B", "C")
#students = Attr.load_students_data(path)
#print(Attr.clean_students_data(students))
