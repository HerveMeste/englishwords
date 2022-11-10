# Debut de l'application de quizz pour le test d'anglais
import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZZ=5
QUESTIONS = {
    "Comment dire en anglais 'Réseau Social' ? ": [
        "Social Network","Network Social","BLABLABLA",
    ],
    "Comment dire en anglais 'Transfert de fichier' ? ": [
        "File transfer","Transfer file","File transfered",
    ],
    "Comment dire en anglais 'Bureau d'assistance' ? ": [
        "Help desk","Office assistance","Help me",
    ],
}

num_questions = min(NUM_QUESTIONS_PER_QUIZZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0

for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict (
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please, answer one of {','.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        num_correct +=1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct answers out of {num} questions")