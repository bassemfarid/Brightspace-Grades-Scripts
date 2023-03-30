#! usr/bin/env python3
"""
Pulls all the major sections from a Brightspace Quiz export file and organizes
it into an Brightspace Grades import file.

Instructions:
Place the exported quiz file in the same folder
Adjust the SECTIONS and parallel GRADES_SUFFIX to how you've formatted the
Quiz sections and Brightspace Grade items
"""

from os import listdir

import pandas as pd

# The sections on your quiz to export to grades
SECTIONS = ["Knowledge & Understanding",
            "Thinking & Inquiry", "Communication", "Application"]

# What the suffix of the quiz grade item should be;
# Must end in " Points Grade" and be parallel to SECTIONS
GRADES_SUFFIX = [" [KU] Points Grade", " [TI] Points Grade",
                 " [C] Points Grade", " [A] Points Grade"]


QUIZ_FILE = [dir for dir in listdir() if " - Attempt Details.xlsx" in dir][0]
QUIZ_NAME = QUIZ_FILE[: QUIZ_FILE.index(" - Attempt Details")]
quiz = pd.read_excel(QUIZ_NAME + " - Attempt Details.xlsx")
quiz = quiz[quiz["Bonus?"].isin(SECTIONS)]
quiz = quiz.iloc[:, [1, -8, -2]]

quiz_import = {"Username": []}
for suffix in GRADES_SUFFIX:
    quiz_import[QUIZ_NAME + suffix] = []
quiz_import["End-of-Line Indicator"] = "#"

prev_row_user = None
for i in range(len(quiz)):
    if quiz.iloc[i, 0] != prev_row_user:
        prev_row_user = quiz.iloc[i, 0]
        quiz_import["Username"].append(prev_row_user)
    SECTION_IND = SECTIONS.index(quiz.iloc[i, 1])
    QUIZ_GRADE_NAME = QUIZ_NAME + GRADES_SUFFIX[SECTION_IND]
    quiz_import[QUIZ_GRADE_NAME].append(quiz.iloc[i, 2])

pd.DataFrame(quiz_import).to_csv(QUIZ_NAME + " import.csv", index=False)
