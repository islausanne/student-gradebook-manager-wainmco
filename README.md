# 🗂️ Student Gradebook Manager
**IB Computer Science – B2.5.1 File Processing**

## Overview
In this project, you will build a simple **command-line gradebook manager**.  
It will allow a teacher to **add, view, search, and update student records** stored in a text file.  
The goal is to learn how to **read from**, **write to**, and **append to** text files using Python.

By the end, you should understand how file processing allows a program to **store data permanently** — even after it stops running.

---

## Learning Goals
By completing this project, you will:
- Use `open()` with different modes (`"r"`, `"w"`, `"a"`)
- Read and write text files using `readline()`, `readlines()`, and `write()`
- Close files safely using `with open() as file:`
- Handle basic data parsing (splitting text into lists)
- Use error handling (`try`, `except`) when files are missing

---

## 🧩 Starter File
Create a new text file called **`grades.txt`** with this sample data:

```
Alice,85
Ben,72
Carlos,91
Dana,66
```

Each line represents a student’s name and grade, separated by a comma.

---

## 🧠 Step 1: Display all records
Write a program that:
1. Opens `grades.txt` in **read** mode.
2. Reads each line using a loop.
3. Splits the name and grade using `.split(",")`.
4. Prints them in a clear format such as:
   ```
   Alice: 85
   Ben: 72
   Carlos: 91
   Dana: 66
   ```

✅ **Success check:** The program correctly displays all students from the file.

---

## ✍️ Step 2: Add a new record
Extend your program so that it:
1. Asks the user for a **name** and **grade**.
2. Opens `grades.txt` in **append** mode (`"a"`).
3. Writes a new line to the file with the format `"Name,Grade"`.

✅ **Success check:** After running the program again, the new record should appear at the end of the file.

---

## 🔍 Step 3: Search for a student
Add a menu option to **search** for a student by name:
1. Ask the user for a name.
2. Loop through the file to find that name.
3. If found, display their grade; otherwise print `"Student not found"`.

✅ **Success check:** Searching for “Ben” should display “Ben: 72”.

---

## 🧹 Step 4: Update or remove a student (Challenge)
To change a student’s grade or remove them:
1. Read all lines into a list.
2. Modify or remove the matching record.
3. Open the file in **write** mode (`"w"`) and rewrite the updated list.

✅ **Success check:** The file updates correctly when you re-open it.

---

## 🧾 Step 5: Calculate class statistics (Extension)
- Calculate the **average grade** and save it to a new file `summary.txt`.
- Add a timestamp to the file using Python’s `datetime` library.

Example line in `summary.txt`:
```
Class average: 78.5 (calculated on 2025-10-08)
```

---

## 🧠 Reflection (for your design folder)
Write a short paragraph in your notes explaining:
- What each file mode (`r`, `w`, `a`) does.
- Why context managers (`with open(...)`) are safer than using `close()`.
- How your program demonstrates reading, writing, and appending.

---

**Extension ideas:**
- Add input validation (grades must be between 0–100).
- Sort students alphabetically or by grade.
- Add colour to terminal output using the `colorama` library.
- Log every action (add, update, delete) to a `log.txt` file using append mode.

---

*This project covers the IB Computer Science topic **B2.5.1 – File Processing.***
