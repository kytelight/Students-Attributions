import csv
from rule_engine import Rule, Context, resolve_attribute
import re


class Class:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other): 
        return self.name == other.name


class Student:
    
    def __init__(self, ID, name, sex, age, IQ, assiduity_score, nationality, school):
        self.ID = ID
        self.name = name
        self.sex = sex
        self.age = age
        self.IQ = IQ
        self.assiduity_score = assiduity_score
        self.nationality = nationality
        self.school = school


class Actions:

    def __init__ (self, logic):
        self.logic = logic

    def compute_class(self, rules, rule):
        """
        Find the class that corresponds to a rule
        """
        return self.logic[rules.index(rule)]

    def match_ID_class(self, allocations, match_ID, rules, rule):
        """
        Find the class that corresponds to a rule
        """
        return allocations.setdefault(
            match_ID, self.compute_class(rules, rule)
        )
        

class Allocations:

    def __init__ (self, allocations):
        self.allocations = allocations

    @staticmethod
    def convert_rules_rule_engine(rules):
        """
        Convert into rule objects to be parsed by rule engine 
        """
        # Declare context
        context = Context(resolver=resolve_attribute)
        
        # Convert rules
        reng_rules = {}
        for parent_rule, child_rules in rules.items():

            # convert child rules to rules_engine rule
            reng_child_rules = []
            for child_rule in child_rules:
                reng_child_rules.append(Rule(child_rule, context=context))

            # convert child rules to rules_engine rule
            reng_rules[Rule(parent_rule, context=context)] = reng_child_rules
        
        return reng_rules

    @staticmethod
    def convert_rules_if_statements(rule):
        """
        Convert into rules to be evaluated
        """
        return re.sub(
            r'\b(IQ|age|sex|assiduity_score|nationality|school)\b', 
            r'student.\1',
            rule
        )

    def allocate_students_rule_engine(self, actions, rules, students):
        """
        Allocate students to their respective classes using 
        rule engine
        """

        # Convert rule to "rule_engine" rule
        reng_rules = Allocations.convert_rules_rule_engine(rules)

        # Allocate students
        for parent_rule, child_rules in reng_rules.items():

            # Match students to parent rule
            matche1 = list(parent_rule.filter(students))
            for child_rule in child_rules:

                # Match students to child rules
                for match2 in child_rule.filter(matche1):

                    # Execute actions
                    actions.match_ID_class(
                        self.allocations, match2.ID, child_rules, child_rule
                    )

        return self.allocations


    def allocate_students_if_statements(self, rules, students):
        """
        Allocate students to their respective classes using 
        conditional branching
        """
        for student in students:
            
            # Evaluate parent rules
            if (eval(Allocations.convert_rules_if_statements(list(rules.keys())[0]))):

                # Evaluate child rules
                if (eval(Allocations.convert_rules_if_statements(list(rules.values())[0][0]))):
                    self.allocations[student.ID] = Class("A")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[0][1]))):
                    self.allocations[student.ID] = Class("B")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[0][2]))):
                    self.allocations[student.ID] = Class("C")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[0][3]))):
                    self.allocations[student.ID] = Class("D")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[0][4]))):
                    self.allocations[student.ID] = Class("E")

                else:
                    self.allocations[student.ID] = Class("F")

            elif (eval(Allocations.convert_rules_if_statements(list(rules.keys())[1]))):

                if (eval(Allocations.convert_rules_if_statements(list(rules.values())[1][0]))):
                    self.allocations[student.ID] = Class("A")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[1][1]))):
                    self.allocations[student.ID] = Class("B")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[1][2]))):
                    self.allocations[student.ID] = Class("C")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[1][3]))):
                    self.allocations[student.ID] = Class("D")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[1][4]))):
                    self.allocations[student.ID] = Class("E")

                else:
                    self.allocations[student.ID] = Class("F")

            else:

                if (eval(Allocations.convert_rules_if_statements(list(rules.values())[2][0]))):
                    self.allocations[student.ID] = Class("A")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[2][1]))):
                    self.allocations[student.ID] = Class("B")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[2][2]))):
                    self.allocations[student.ID] = Class("C")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[2][3]))):
                    self.allocations[student.ID] = Class("D")

                elif (eval(Allocations.convert_rules_if_statements(list(rules.values())[2][4]))):
                    self.allocations[student.ID] = Class("E")

                else:
                    self.allocations[student.ID] = Class("F")
                    
        return self.allocations

class DataHandler:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_students(self):
        """
        Load data into a list of students objects
        """
        students = []
        with open(self.file_path, mode="r") as file:

            reader = csv.DictReader(file)

            # Load data from frile_path 
            for student in reader:

                # Convert columns to appropriate data types
                student = Student(
                    int(student["ID"]),
                    str(student["name"]),
                    str(student["sex"]),
                    int(student["age"]),
                    int(student["IQ"]),
                    int(student["assiduity_score"]),
                    str(student["nationality"]),
                    str(student["school"])
                )

                # Add to students list
                students.append(student)
                
        return students

    def save_students(self, input_path, output_path, allocations):
        """
        Append students dataset with allocated classes and
        save to output_path
        """
        with open(input_path, mode='r') as input_file, \
            open(output_path, mode='w', newline='') as output_file:
            
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(
                output_file, 
                fieldnames=reader.fieldnames + ["class"]
                )

            # Populate headers
            writer.writeheader()

            # Write data to output_path
            for row in reader:
                
                row["class"] = allocations[int(row["ID"])].name
                writer.writerow(row)
