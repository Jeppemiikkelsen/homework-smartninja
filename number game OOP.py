import random
import json
import datetime
import operator

class Result():
    def __init__(self, score, player_name, date):
        self.score = attempts
        self.player_name = name
        self.date = current_time


secret = random.randint(1, 30)
attempts = 0
current_time = datetime.datetime.now()
incorrect_guess = []
print(current_time)

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
for score_dict in score_list[:3]:
    print(str(score_dict["name"]) + ", " + str(score_dict["attempts"]) + " attempts, secret number: " + str(score_dict["answer"]) + ", incorrect guesses:" + str(score_dict["incguess"]) + ", date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        name = input("Attempts needed: " + str(attempts) + ". Please input your name: ")
        print("You guessed the following numbers: " + str(incorrect_guess) + " which were inccorect.")
        score_list.append({"name": name, "attempts": attempts, "answer": secret, "incguess": str(incorrect_guess), "date": str(datetime.datetime.now())})
        score_list.sort(key=operator.itemgetter("attempts"))
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        resultat = Result(score=attempts, player_name=name, date=current_time)
        with open("results.txt", "w") as res_ult:
            res_ult.write(str(resultat.__dict__))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        incorrect_guess.extend([guess])
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        incorrect_guess.extend([guess])
