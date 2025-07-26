# app.py
from qa import generate_answer

if __name__ == "__main__":
    while True:
        query = input("🔎 প্রশ্ন করুন (বা 'exit'): ").strip()
        if query.lower() == "exit":
            break
        print("🧠 উত্তর:", generate_answer(query), "\n")
