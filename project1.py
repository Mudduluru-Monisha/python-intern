questions = [
    {
        "question": "What is the national game of India?",
        "options": ["A. Hockey", "B. Kabaddi", "C. Cricket", "D. Badminton"],
        "answer": "A"
    },
    {
        "question": "What is the national bird in India?",
        "options": ["A. Kiwi", "B. Peacock", "C. Kingfisher", "D. Eagle"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]


def ask_question(question_data):
    """Ask a single question and validate the answer."""
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

    while True:
        user_answer = input("Enter the correct option (A, B, C, or D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    if user_answer == question_data["answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer is {question_data['answer']}.\n")
        return False


def run_quiz(questions):
    """Run the entire quiz and keep score."""
    score = 0
    total_questions = len(questions)

    for question in questions:
        if ask_question(question):
            score += 1

    print(f"Your final score is {score} out of {total_questions}.")


if __name__ == "__main__":
    run_quiz(questions)
