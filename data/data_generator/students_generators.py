# Names generated from: https://www.randomlists.com/random-names?qty=100 


import pandas as pd
import random


# Load names
names = pd.read_csv("Student_Names.csv")

# Initialize the students dataframe
df1 = pd.DataFrame(
    columns=[
        "ID",
        "name",
        "sex",
        "age",
        "IQ",
        "assiduity_score",
        "nationality",
        "school",
    ]
)

ID = 1
for _, name in names.iterrows():

    # Add male and female rows
    df2 = pd.DataFrame(
        [
            [
                ID,
                name["Male"],
                "Male",
                random.randint(15, 23),
                random.randint(70, 140),
                random.randint(1, 5),
                random.choices(["Home", "International"], weights=[35, 15])[0],
                random.choices(["Rainbow High", "Cape Coral High"], weights=[25, 25])[0]    
            ],
            [
                ID + 1,
                name["Female"],
                "Female",
                random.randint(15, 23),
                random.randint(70, 140),
                random.randint(1, 5),
                random.choices(["Home", "International"], weights=[35, 15])[0],
                random.choices(["Rainbow High", "Waterfalls School for Girls", "Cape Coral High"], weights=[10, 30, 10])[0]

            ],
        ],
        columns=[
            "ID",
            "name",
            "sex",
            "age",
            "IQ",
            "assiduity_score",
            "nationality",
            "school",
        ],
    )

    # Append to dataframe
    df1 = pd.concat([df1, df2])

    ID += 2

# Shuffle dataframe
df1 =  df1.sample(frac=1)

# Write to csv file
df1.to_csv("Data/students_dataset.csv", index=False)
print("Dataset created in Data/")
