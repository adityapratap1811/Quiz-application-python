
import time

# Quiz questions, options, and correct answers
quiz = [
    {
        "question": "Which language is known as the father of programming?",
        "options": ["A. Python", "B. C", "C. Java", "D. Fortran"],
        "answer": "D"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Text Markup Language", "B. High Tech Machine Learning", "C. Hyperlinks and Text Markup Level", "D. Home Tool Markup Language"],
        "answer": "A"
    },
    {
        "question": "Which data structure uses FIFO (First In First Out)?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    }
]

score = 0
time_per_question = 15  # seconds allowed per question

print("📝 Welcome to the Quiz Application!")
print("You have", time_per_question, "seconds for each question.\n")

for i, q in enumerate(quiz, 1):
    print(f"Q{i}: {q['question']}")
    for opt in q["options"]:
        print(opt)

    start_time = time.time()
    user_answer = None

    # Timer loop
    while True:
        if time.time() - start_time > time_per_question:
            print("⏰ Time's up! Moving to next question.\n")
            break
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            if user_answer == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print("❌ Wrong! Correct answer was", q["answer"], "\n")
            break
        else:
            print("Please enter a valid option (A/B/C/D).")

print("🎯 Quiz Completed!")
print("Your Final Score:", score, "/", len(quiz))
if score == len(quiz):
    print("🔥 Excellent! You nailed it!")
elif score >= len(quiz)//2:
    print("👍 Good job! Keep practicing.")
else:
    print("📖 Better luck next time, keep learning!")
