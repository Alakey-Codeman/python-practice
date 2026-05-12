tasks = input('Cколько задач решил? ')
try:
    tasks = int(tasks)
except ValueError:

    print('Введите корректное значение в следующий раз, приколист')
    quit()
mistakes = input('Cколько сделал ошибок? ')
try:
    mistakes = int(mistakes)
except ValueError:

    print('Введите корректное значение в следующий раз, приколист')
    quit()
time = input('Cколько минут потратил? ')
try:
    time = int(time)
except ValueError:

    print('Введите корректное значение в следующий раз, приколист')
    quit()
accuracy = (tasks - mistakes)/tasks * 100
if accuracy < 0:
    print('Ты что-то напутал')
    quit()
elif accuracy >= 90:
    print('Отличный уровень')
elif accuracy >= 70:
    print('Хороший уровень')
elif accuracy >= 50:
    print('Нужно больше практики')
else: print('Срочно повторить тему')

if accuracy < 60:
    if time < 10:
        print('Похоже, ты слишком спешил')
elif accuracy > 95:
    if time < 15:
        print('Ты машина!')
else: print('Твоя оценка:')

if accuracy > 90:
        print('Mark A')
elif accuracy > 80:
        print('Mark B')
elif accuracy > 70:
        print('Mark C')
else: print('Mark D')
quit()