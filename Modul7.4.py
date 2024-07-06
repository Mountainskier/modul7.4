team1_num = 3  # Мастера кода
team2_num = 3  # Волшебники данных
score_1 = 55  # Мастера кода
score_2 = 55  # Волшебники данных
team1_time = 3223.322  # Мастера кода
team2_time = 3223.322  # Волшбники


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'


tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print("В команде Мастера кода участников: %d !" % team1_num)
print("В команде Волшебники данных участников: %d !" % team2_num)
print("Итого сегодня участников: %d и %d !\n" % (team1_num, team2_num))

print("Команда Мастера кода решила задач {} !".format(score_1))
print("Мастера кода решили задачи за {} с!".format(team1_time))
print("Команда Волшебники данных решила задач {} !".format(score_2))
print("Волшебники данных решили задачи за {} с!\n".format(team2_time))

print(f"Команды решила {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result()}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунд на задачу!")
