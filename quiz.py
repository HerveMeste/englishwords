import random
from string import ascii_lowercase
import pathlib

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Présentation du jeu
print("Welcome to the game called 'Quizz Game'")
print("\nYou can play to practice your english and your technical vocabulary.")
print("\n\nGood Game ! ;)")
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

print("\nIMPORTANT ! "
      "\n Si vous voyez ceci '?' dans les réponses, alors ça vous donnera un indice en tapant '?' dans les choix.")


def prepare_questions():
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        topic_info = tomllib.loads(f.read())
        topics = {
            topic["label"]: topic["questions"] for topic in topic_info.values()
        }
        topic_label = get_answers(
            question="\nWhich topic do you want to be quizzed about ?",
            alternatives=sorted(topics),
        )[0]

        # Compter les questions pour les developpeur ou pour les réseaux
        data = QUESTIONS_PATH.read_text()
        questions_network = data.count("network.questions")
        questions_dev = data.count("dev.questions")

        # Choisir le nombre de question en fonction du choix fait
        if topic_label == "Dev":
            total_question = questions_dev
        elif topic_label == "Network":
            total_question = questions_network

        questions = topics[topic_label]
        numbers_questions = int(
            input(f"How many questions do you want ? You can choose a maximum of {total_question} questions: \n"))
        num_questions = min(numbers_questions, len(questions))
        return random.sample(questions, k=num_questions)


def get_answers(question, alternatives, num_choices=1, hint=None):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    if hint:
        labeled_alternatives["?"] = "Astuce"
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        if any(
                (invalid := answer) not in labeled_alternatives
                for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]


def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    if set(answers) == set(correct_answers):
        print("⭐ Correct! ⭐")
        return 1
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))
        return 0


def run_quiz():
    questions = prepare_questions()

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    # Détermination des notes en fonction des réponses
    note = (100 * num_correct) / num
    if note >= 80:
        print("\nYou have obtained the grade A.")
    elif 60 <= note < 80:
        print("\nYou have obtained the grade B.")
    elif 40 <= note < 60:
        print("\nYou have obtained the grade C.")
    elif 0 <= note < 40:
        print("\nYou have obtained the grade D.")

    print(f"\nYou got {num_correct} correct out of {num} questions")


if __name__ == "__main__":
    run_quiz()
