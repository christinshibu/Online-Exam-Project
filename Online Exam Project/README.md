# Online Exam Project

A simple command-line based online examination system built in Python. This project simulates a timed multiple-choice quiz with secure login, live timer, and professional result reporting.

## Features

- **Secure Login System**: User authentication with username and password stored in `students.txt`
- **Timed Exams**: Configurable exam duration with live countdown timer
- **Multiple-Choice Questions**: Pre-defined question bank with randomized order
- **Live Input Tracking**: Real-time keyboard input during questions
- **Professional Reports**: Detailed result cards saved to `results.txt` with pass/fail status
- **Cross-Platform Compatibility**: Designed for Windows (uses `msvcrt` for keyboard handling)

## Requirements

- Python 3.x
- Windows operating system (due to Windows-specific keyboard input handling)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd online-exam-project
   ```

2. Ensure Python 3.x is installed on your system.

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Login with valid credentials (default: admin/123 or student/pass123)

3. Take the exam by answering the multiple-choice questions within the time limit

4. View results in `results.txt` after completion

## File Structure

- `main.py`: Main application script containing exam logic, timer, and login system
- `students.txt`: Text file containing user credentials (username,password format)
- `results.txt`: Output file for exam results and reports

## Configuration

- **Exam Duration**: Modify `exam_duration` variable in `main.py` (default: 60 seconds)
- **Questions**: Edit the `questions` list in `main.py` to add/modify exam questions
- **Credentials**: Update `students.txt` to manage user accounts

## Sample Output

```
=== SECURE LOGIN SYSTEM ===
Enter Username: student
Enter Password: pass123
Login Successful!

=== EXAMINATION STARTED: STUDENT ===
Total Questions: 4 | Duration: 60s

Q1: Which data type is used to store multiple items in a single variable?
  A. Integer
  B. List
  C. Float
[ TIME LEFT: 55s ] Your Answer: B
------------------------------
...
```

## License

This project is open-source. Feel free to modify and distribute.