import time
import os
import sys
import threading
import random
from datetime import datetime

# Windows-specific import for live keyboard tracking
if os.name == 'nt':
    import msvcrt

# --- 1. Terminal Styling ---
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

# --- 2. Global Variables ---
stop_timer = False
exam_duration = 60  # Total time for the entire exam in seconds

# --- 3. Question Bank ---
# Questions stored in a list of dictionaries
questions = [
    {"q": "Which data type is used to store multiple items in a single variable?", "options": ["A. Integer", "B. List", "C. Float"], "answer": "B"},
    {"q": "What is the correct syntax to output 'Hello' in Python?", "options": ["A. p('Hello')", "B. echo('Hello')", "C. print('Hello')"], "answer": "C"},
    {"q": "What is 10 // 3 in Python?", "options": ["A. 3.33", "B. 3", "C. 3.0"], "answer": "B"},
    {"q": "Which keyword is used to create a function?", "options": ["A. def", "B. function", "C. define"], "answer": "A"}
]

# --- 4. Professional Result Structure ---
def save_professional_report(name, score, total):
    percentage = (score / total) * 100
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    status = "PASS" if percentage >= 50 else "FAIL"
    
    # Structured multiline string for the report card
    report_card = f"""
==================================================
         ONLINE EXAMINATION REPORT CARD         
==================================================
 DATE/TIME    : {date_time}
 STUDENT NAME : {name.upper()}
--------------------------------------------------
 TOTAL QUESTIONS    : {total}
 CORRECT ANSWERS    : {score}
 SCORE PERCENTAGE   : {percentage:.2f}%
 FINAL STATUS       : {status}
==================================================
\n"""
    
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(report_card)

# --- 5. Live Timer & Input Logic ---
def live_timer_thread(timeout, start_time):
    """Background thread that updates the clock every second."""
    global stop_timer
    while not stop_timer:
        elapsed = time.time() - start_time
        remaining = timeout - elapsed
        if remaining <= 0:
            break
        # \r allows the line to overwrite itself for a 'live' effect
        sys.stdout.write(f"\r{Color.YELLOW}[ TIME LEFT: {int(remaining)}s ]{Color.END} Your Answer: ")
        sys.stdout.flush()
        time.sleep(1)

def get_input_with_live_timer(timeout, start_time):
    global stop_timer
    stop_timer = False
    
    # Start the background timer thread
    timer_worker = threading.Thread(target=live_timer_thread, args=(timeout, start_time))
    timer_worker.daemon = True
    timer_worker.start()

    user_input = ""
    while True:
        if (time.time() - start_time) > timeout:
            stop_timer = True
            return None  # Signal for auto-submission

        if msvcrt.kbhit():
            char = msvcrt.getche().decode('utf-8')
            if char in ['\r', '\n']:  # User pressed Enter
                stop_timer = True
                print() # Move to next line
                return user_input
            user_input += char
        time.sleep(0.05)

# --- 6. Main Exam Logic ---
def run_exam(student_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Color.PURPLE}{Color.BOLD}=== EXAMINATION STARTED: {student_name.upper()} ==={Color.END}")
    print(f"Total Questions: {len(questions)} | Duration: {exam_duration}s\n")
    
    score = 0
    random.shuffle(questions) # Additional feature: Randomization
    exam_start = time.time()

    for i, q in enumerate(questions):
        remaining_total = exam_duration - (time.time() - exam_start)
        
        if remaining_total <= 0:
            print(f"\n{Color.RED}⏰ TIME EXPIRED! Auto-submitting...{Color.END}")
            break

        print(f"{Color.BOLD}Q{i+1}: {q['q']}{Color.END}")
        for opt in q['options']:
            print(f"  {opt}")
        
        # Get input while the timer ticks live
        ans = get_input_with_live_timer(remaining_total, exam_start)
        
        if ans is None: # Time ran out while waiting for input
            break
            
        if ans.upper().strip() == q['answer']:
            score += 1
        
        print("-" * 30)

    # Save and display final results
    save_professional_report(student_name, score, len(questions))
    print(f"\n{Color.GREEN}{Color.BOLD}Exam finished. Results logged to results.txt{Color.END}")

# --- 7. Login Module ---
def student_login():
    # Create dummy credentials file if missing
    if not os.path.exists("students.txt"):
        with open("students.txt", "w") as f:
            f.write("admin,123\nstudent,pass123")

    print(f"{Color.CYAN}{Color.BOLD}=== SECURE LOGIN SYSTEM ==={Color.END}")
    username = input("Enter Username: ")
    password = input("Enter Password: ") # Consider getpass.getpass() for security
    
    with open("students.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if username == u and password == p:
                print(f"{Color.GREEN}Login Successful!{Color.END}\n")
                return username
    print(f"{Color.RED}Invalid Credentials.{Color.END}")
    return None

# --- Main Entry Point ---
if __name__ == "__main__":
    if os.name == 'nt':
        os.system('color') # Enable ANSI colors in Windows CMD
        
    user = student_login()
    if user:
        run_exam(user)