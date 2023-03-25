import unittest
from StudentsAttributions import Class, Allocations, DataHandler, Actions


class TestRulesMethods(unittest.TestCase):

    def setUp(self):
       
       # Inputs
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
        students = DataHandler(
            "C:/Users/ayar9/source/repos/Data/students_dataset.csv"
            ).load_students()
        
        # Allocations
        self.alloc = (Allocations({})
                      .allocate_students_rule_engine(actions, rules, students))

    def test_rainbow_high_rules(self):

        self.assertEqual(self.alloc[263], Class("A"))
        self.assertEqual(self.alloc[41], Class("B"))
        self.assertEqual(self.alloc[5], Class("C"))
        self.assertEqual(self.alloc[57], Class("D"))
        self.assertEqual(self.alloc[118], Class("E"))
        self.assertEqual(self.alloc[375], Class("F"))


    def test_waterfalls_school_for_girls_rules(self):

        self.assertEqual(self.alloc[374], Class("A"))
        self.assertEqual(self.alloc[42], Class("B"))
        self.assertEqual(self.alloc[348], Class("C"))
        self.assertEqual(self.alloc[282], Class("D"))
        self.assertEqual(self.alloc[30], Class("E"))
    
    def test_cape_coral_high_rules(self):

        self.assertEqual(self.alloc[250], Class("A"))
        self.assertEqual(self.alloc[335], Class("B"))
        self.assertEqual(self.alloc[127], Class("C"))
        self.assertEqual(self.alloc[39], Class("D"))
        self.assertEqual(self.alloc[175], Class("E"))
        self.assertEqual(self.alloc[204], Class("F"))


if __name__ == "__main__":
    unittest.main()