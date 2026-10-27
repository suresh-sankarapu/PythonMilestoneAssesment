
**Problem Statement**
The goal is to build a lightweight, digital Employee Management System that can automatically store employee data in a computer file, read that data, add new members, and perform basic operations like searching for specific roles or finding the highest earner.

**Approach / Logic Used**
The program follows a clear step-by-step logic to manage the data:
• Object-Oriented Setup: Instead of dealing with random pieces of text, the code uses a blueprint (a Class) to bundle an individual employee's ID, Name, Role, and Salary into a single object.
• Persistent File Storage: Data is stored inside a plain text file (employees.txt). This ensures the data isn't lost when the program closes.
• String Parsing: When reading the text file, the program splits each line by commas (,) to separate individual pieces of information.
• Filtering & Aggregation Loops: The code uses loops to scan through the list of employees one by one to check conditions (e.g., Is the salary > 50,000? or Does the role match 'Tester'?) and counts occurrences using a dictionary mapping.

**How to Run the Program**
1. Make sure you have Python installed on your system.
2. Copy your code and save it in a file named main.py.
3. Open your terminal, command prompt, or code editor (like VS Code or PyCharm).
4. Run the file using the following command:bash
python main.py
Use code with caution.
5. The code will automatically create an employees.txt file in the same folder and print the analyzed results to your screen.

**Sample Input**
The program automatically creates its own input by writing these rows into employees.txt:
text
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000


**Sample Output**
Employee File created successfully
 All employee details:
101 - Rahul - Python Developer - 50000
102 - Anjali - Tester - 45000
103 - John - Developer - 60000
104 - Priya - Tester - 48000

Employee earning more than 50000
103 - John - Developer - 60000

Employees in the role: Tester
102 - Anjali - Tester - 45000
104 - Priya - Tester - 48000

Employee with the highest salary
103 - John - Developer - 60000

Employee count by role
Python Developer : 1
Tester : 2
Developer : 1


**Python Concepts Used**
• Object-Oriented Programming (OOP): Creating a class Employee with an __init__ constructor method to model real-world data objects.
• File Handling (open, r, w, a): Using Python's with open() syntax to safely write (w), append (a), and read (r) data from a text file without corrupting it.
• The os Module: Using os.path.join and os.path.dirname(__file__) to dynamically figure out exactly where the script is running so it never breaks with a "File Not Found" error.
• String Manipulation (strip & split): Using .strip() to clean up hidden spacing/newlines and .split(",") to break a comma-separated text line into an accessible list of data pieces.
• Lambda Functions: The expression key=lambda emp: emp.salary acts as a quick, one-line function telling Python's max() tool exactly which attribute to look at when calculating the highest earner.
• Dictionaries (role_count): Storing information as key-value pairs (e.g., 'Tester': 2) and using the .get() method to cleanly count occurrences without triggering errors for missing items.

