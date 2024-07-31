
# Quiz Game in Python

# Sample questions (you can add more!)
questions = [
    {
        "question": "What's the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What's the capital of india?",
        "options": ["Delhi", "London", "New delhi", "Madrid"],
        "answer": "New delhi"
    },
    {
        "question": "Which famous scientist developed the theory of general relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
        "answer": "Albert Einstein"
    },
    {
        "question": "Who wrote the famous play “Romeo and Juliet?",
        "options": ["William Wordsworth", "William Shakespeare", "Jane Austen", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
]

# Initialize score
score = 0

# Quiz loop
for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")

    user_choice = input("Enter the number corresponding to your answer: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 1 <= user_choice <= len(q["options"]):
            if q["options"][user_choice - 1] == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Oops! The correct answer was: {q['answer']}\n")
        else:
            print("Invalid choice. Try again.\n")
    else:
        print("Invalid input. Try again.\n")

# Display final score
print(f"Your score: {score}/{len(questions)}")



