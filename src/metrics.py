import pandas as pd
from statistics import mean

def evaluation_question(question, question_answers, answer):
    best_answer = question_answers[0]['score']
    for i in range(0, len(question_answers)) :
        if question_answers[i]['score'] > best_answer :
            best_answer = question_answers[i]['score']
    result = abs(best_answer - answer['score'])
    return "Le résultat doit être le plus proche de 0: " + str(result)

def evaluation_un(score_best_answer, score_chosen) :
    result = abs(score_best_answer - score_chosen)
    return "Le résultat doit être le plus proche de 0: " + str(result)

def evaluation(best_scores, chosen_scores):
    results = []
    bestScores = best_scores.tolist()
    chosenScores = chosen_scores.tolist()
    for i in range(0, len(bestScores)):
        results.append(abs(bestScores[i] - chosenScores[i]))
    average = mean(results)
    return "Le résultat doit être le plus proche de 0: " + str(average)

# © Marianne SEBILLE 2021