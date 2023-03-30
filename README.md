# Brightspace Grades Scripts
Python scripts to process data for easy grade importing.

## Quiz to Grades
### Problem
Brightspace Quiz can only have one grade association, the overall mark of the quiz. Associating sections of a quiz manually to multiple grade items is a tedious task, especially when randomizing the quiz.

### Solution
On the quiz grading section, Export to Excel, process using quiztogrades and use the created import file to import to grades as a .csv.

### Setup
Requirements: Python 3
1. Clone this repository to a folder. Create a environment or use global.
2. Install the required pip packages using `pip3 install -r requirements.txt` in terminal

### Usage
1. Download the required Excel file by using the Export to Excel button in the Quiz's Grading page. Place it into the same folder as the script.
2. In the script, make sure SECTIONS and GRADES_SUFFIX is set and parallel. Run the script.
3. Upload the newly created import file in the Grades section of Brightspace using the Import button. I suggest to already have the grade item created and have 'Create a new grade item' unchecked to avoid potential problems.
