import copy
import json
import random
import time



POSSIBLE_ANSWERS = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}


def change_highscore():
    pass


def run_game(player: dict, questions_path: str = "questions.json") -> int:
    score = 0
    with open(questions_path, "r") as f:
        questions = json.loads(f.read())
        questions = questions['questions']
        copy_questions = copy.deepcopy(questions)
    while copy_questions:
        question_object = random.choice(copy_questions)
        print(question_object)
        print(question_object['question'])
        for index, answer in enumerate(question_object['answers']):
            print(f"{POSSIBLE_ANSWERS[index]} {answers}")
            
            pick = input("Alege raspunsul corect: ")
        answers = {v: k for k, v in POSSIBLE_ANSWERS.items()}
        if answers[f"{pick}."] == question_object['correctIndex']:
            print("Correct answer")
            score += 1
        else:
            print("Wrong answer")

        # print(question_id)
        copy_questions.remove(question_object)
        time.sleep(3)

    print(f"You have answered to {score} questions correctly.")
    
    if score > player['high_score']:
        change_highscore()