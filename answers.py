from collections import ChainMap as cm

answers = {"привет": "И тебе привет!",
           "как дела": "Лучше всех",
           "пока": "Увидимся"}


def get_answer(question, answers):
    return answers.get(question, "Not found").lower()


question = input("Type it: ")

print(get_answer(question, answers))


# chainmap testing default values bla-bla
answers_default = {"preved": "medved", "привет": "ХА-ХА"}
del answers["привет"]
answers_cm = dict(cm(answers, answers_default))
print(get_answer(question, answers_cm))
