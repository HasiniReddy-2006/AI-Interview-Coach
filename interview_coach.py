import json
import random

def load_questions(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def get_questions_by_category(questions, category):
    return [q for q in questions if q['category'] == category]

def get_random_question(questions):
    return random.choice(questions)

def generate_feedback(user_answer):
    # Simple feedback example: check if answer is long enough
    if len(user_answer.split()) < 10:
        return "Try to give more detailed answers with examples."
    else:
        return "Great! Your answer is detailed and clear."

def save_answer_and_feedback(filename, question, answer, feedback):
    data = {
        'question': question,
        'answer': answer,
        'feedback': feedback
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\n✅ Your answer and feedback have been saved to '{filename}'")

def main():
    questions = load_questions('questions.json')

    print("Choose a category: behavioral, technical, hr")
    category = input("Enter category: ").strip().lower()

    filtered_questions = get_questions_by_category(questions, category)

    if not filtered_questions:
        print(f"No questions found for category '{category}'. Exiting.")
        return

    question = get_random_question(filtered_questions)
    print(f"\nHere's your question ({category}):")
    print(question['question'])

    answer = input("\nType your answer below:\n")

    feedback = generate_feedback(answer)

    print("\n💡 Simulated AI Feedback:")
    print(f"- {feedback}")

    save_answer_and_feedback('my_answer.json', question['question'], answer, feedback)

if __name__ == "__main__":
    main()
