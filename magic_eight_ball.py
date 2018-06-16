import random

#List of possible answers from https://en.wikipedia.org/wiki/Magic_8-Ball
ANSWER_LIST = ["It is certain", "It is decidendly so",
               "Without doubt", "Definately", "You may rely on it",
               "As I see it, yes", "Most likely", "Yes",
               "All signs point to yes", "Outlook good",
               "It is not certain", "Definately not",
               "You can't rely on it", "As I see it, no", "No",
               "Unlikely", "Maybe", "It is possible", "I doubt it",
               "Try again later"]

def generate_answer():
    answer = ANSWER_LIST[random.randint(0, len(ANSWER_LIST) - 1)]
    return answer

def get_question():
    print("What would you like to ask? ")
    question = input()
    return question

if __name__ == "__main__":
    # execute only if run as a script
    print("Welcome to the Magic 8 Ball!")
    get_question()
    print(generate_answer())
