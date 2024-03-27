import json

import game

MENU = """"
1. Add question
2. Remove question"""


def add_question(all_questions: list, questions_path: str = "questions.json"):
    try:
        new_question = input("Add a new question: ")
        possible_answers = input("Add all the answers, separated by ;. Add them here: ").split(";")
        for index, answer in enumerate(possible_answers):
            print(f"{index}, {answer}")
        correct_answer = input("Introdu una din cifre pentru raspunsul corect: ")

        new_question_obj = {"question": new_question, "answers": possible_answers, "correctIndex": correct_answer}
        all_questions.append(new_question_obj)

        with open(questions_path, "w") as f:
            f.write(json.dumps({'questions': all_questions}, indent=4))

    except Exception as e:
        print(f"Error on adding a new question {e}")

def delete_question():
    pass



def change_correct_answer():
    pass


def run():
    print(MENU)
    admin_pick = input("Alege o optiune: ")
    questions = game.read_questions()
    match admin_pick:
        case "1":
            add_question(questions)
        case "2":
            pass
        case _:
            exit()


if __name__ == '__main__':
    run()