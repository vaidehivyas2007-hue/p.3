<div align="center">

# -- ! Student Data Organizer ! --
### *Interactive Console-Based Student Record Management System*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Collections](https://img.shields.io/badge/Collections-Dictionary%20%26%20List-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Match](https://img.shields.io/badge/Control%20Flow-Match%2FCase-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Data is the new oil — and organizing it well is the first step to mastering it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📖 Menu Options Explained](#-menu-options-explained)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🐛 Known Issues & Fixes](#-known-issues--fixes)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Student Data Organizer** is a beginner-friendly, interactive Python console application that demonstrates core programming concepts such as **dictionaries**, **lists**, **match-case control flow**, **CRUD operations**, and **set-based data deduplication**. The program presents a menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:
- Strengthen understanding of Python dictionaries and list manipulation
- Practice user input handling and menu-driven program design
- Apply CRUD (Create, Read, Update, Delete) logic on in-memory data
- Demonstrate real-world use of Python's `match-case` statement (Python 3.10+)
- Use sets to extract unique values from nested data

---

## 🎯 Problem Statement

> **Objective:** Build a console-based student record management system using Python collections.

You are building a utility program that allows users to manage student data interactively. The program stores student records in memory using a list of dictionaries, and allows the user to add, view, update, delete, and analyze student data through a clean menu-driven interface.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Add Student | CRUD — Create | Collects and stores student details in a dictionary |
| Display All Students | CRUD — Read | Prints all stored records in a formatted layout |
| Update Student Info | CRUD — Update | Finds a student by ID and updates specific fields |
| Delete Student | CRUD — Delete | Removes a student record by ID |
| Display Subjects | Set Operation | Extracts unique subjects offered across all students |

The goal is to demonstrate **fundamental Python data structure skills** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📋 **Dictionary-Based Records** | Each student stored as a structured Python dictionary |
| ✏️ **Field-Level Updates** | Users can update individual fields without re-entering all data |
| 🗑️ **ID-Based Deletion** | Student records are deleted by matching their unique ID |
| 🎓 **Subject Deduplication** | Uses Python `set` to display only unique subjects |
| 🖥️ **CLI Interface** | Simple, clean text-based menu for user interaction |
| 🔀 **Match-Case Control Flow** | Uses Python 3.10+ `match` statement for clean branching |
| ⚠️ **Not Found Handling** | Reports clearly when a searched student ID does not exist |

---

## 🏗️ Project Structure

```
📦 student-data-organizer/
│
├── 📄 project-3.py          ← Main Python script (entry point)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌────────────────────────────────┐
│     Display Main Menu          │  ← 6 options presented to user
└──────────────┬─────────────────┘
               │
   ┌───────────┼────────────┐
   ▼           ▼            ▼
┌──────┐   ┌──────┐    ┌──────┐
│ Add  │   │ View │    │Update│  ...and more
│  1   │   │  2   │    │  3   │
└──┬───┘   └──┬───┘    └──┬───┘
   │          │            │
   ▼          ▼            ▼
┌────────────────────────────────┐
│    Perform Action & Print      │
│         Result                 │
└──────────────┬─────────────────┘
               │
               ▼
       Loop Back to Menu
               │
        (Choice: 6) Exit ✅
```

---

## 📖 Menu Options Explained

### ➕ 1. Add Student

Prompts the user for the following details and stores them in a dictionary appended to the `students` list:

| Field | Type | Example |
|-------|------|---------|
| Student ID | Integer | `101` |
| Name | String | `Ayush` |
| Age | Integer | `20` |
| Grade | String | `A` |
| Date of Birth | String (YYYY-MM-DD) | `2004-05-12` |
| Subjects | String (comma-separated) | `Math, Science, English` |

**Logic:**
```python
student = {
    "identity": student_id,
    "name": name,
    "age": age,
    "grade": grade,
    "dob": dob,
    "subjects": subjects_input
}
students.append(student)
```

---

### 📋 2. Display All Students

Iterates over the `students` list and prints each record in a single formatted line.

**Sample Output:**
```
--- Display All Students ---
Student ID: 101 | Name: Ayush | Age: 20 | Grade: A | DOB: 2004-05-12 | Subjects: Math, Science
```

---

### ✏️ 3. Update Student Information

Searches for a student by ID and opens a sub-menu to update individual fields.

**Updatable Fields:**

| Option | Field |
|--------|-------|
| 1 | Name |
| 2 | Age |
| 3 | Grade |
| 4 | Date of Birth |
| 5 | Subjects |
| 6 | Back to main menu |

---

### 🗑️ 4. Delete Student

Accepts a Student ID, searches for the matching record, and removes it using `list.remove()`.

```python
for stu in students:
    if stu["identity"] == student_id:
        students.remove(stu)
        found = True
```

---

### 🎓 5. Display Subjects Offered

Collects all subjects across every student record and uses a **Python set** to deduplicate them, showing only unique subjects.

```python
all_subjects = set()
for stu in students:
    all_subjects.update(stu["subjects"])
print(all_subjects)
```

---

### 🚪 6. Exit

Prints a goodbye message and breaks the main loop.

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language |
| 📚 **List** | Built-in | Stores all student record dictionaries |
| 🗂️ **Dictionary** | Built-in | Represents each student record |
| 🔀 **Match-Case** | Python 3.10+ | Menu and sub-menu control flow |
| 🔢 **Set** | Built-in | Deduplicates subjects across all records |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |
| 📐 **f-strings** | Python 3.6+ | Formatted student record output |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Add Records** — Students are stored in-memory with all key details
- 📋 **View All Records** — Clean formatted display of all student entries
- ✏️ **Field-Level Updates** — Any individual field can be updated without restarting
- 🗑️ **Delete by ID** — Precise removal of unwanted records
- 🎓 **Unique Subjects** — Set ensures no duplicate subjects are displayed
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited
- ⚠️ **Not Found Handling** — Clear feedback when a student ID is not found

---

## 🐛 Known Issues & Fixes

The following bugs exist in the current version and should be addressed:

| # | Bug | Location | Fix |
|---|-----|----------|-----|
| 1 | `search_id` stored as `str` but compared with `int` `student_id` variable | Case 3 (Update) | Convert: `if stu["identity"] == int(search_id)` |
| 2 | Delete compares `stu["identity"]` (int) with `student_id` (str from `input()`) | Case 4 (Delete) | Convert: `if stu["identity"] == int(student_id)` |
| 3 | `print("all_subject")` prints the string literal, not the variable | Case 5 (Subjects) | Change to: `print(all_subjects)` |
| 4 | `all_subjects.update(stu["subjects"])` iterates over characters of a string, not subjects | Case 5 (Subjects) | Split subjects first: `stu["subjects"].split(",")` |

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core concepts: lists, dicts, loops, and match-case in one project |
| 🗂️ **Real-World CRUD** | Mimics database-style Create, Read, Update, Delete operations |
| 🔄 **Reusability** | Logic can easily be extended into file-based or database storage |
| 📚 **Educational** | Each feature reinforces a distinct Python collection concept |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add search by name, sort by grade, export to CSV, etc. |
| 📖 **Readable Code** | Clean `match-case` structure makes branching easy to follow |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Ayush Isamaliya

[![GitHub](https://img.shields.io/badge/GitHub-isamaliya16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"A well-organized dictionary is worth a thousand scattered variables."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Collections · CLI Applications · CRUD Logic · Data Structures

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🗂️ [Real Python — Dictionaries](https://realpython.com/python-dicts/) — In-depth dictionary tutorials
- 🔀 [Python Match-Case Guide](https://peps.python.org/pep-0634/) — Structural pattern matching (PEP 634)
- 📐 [GeeksForGeeks — Python Sets](https://www.geeksforgeeks.org/python-sets/) — Set operations and use cases
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 📖 [Python f-strings Guide](https://realpython.com/python-f-strings/) — Formatted string literals
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: June 2026*

</div>
