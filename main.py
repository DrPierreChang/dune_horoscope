# Подключаем модуль случайных чисел
import random

# Заготовка для первого предложения
first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про",
          "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел,"
          " должны помнить про", "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

# выводим знаки зодиака
print("1 — Овен")
print("2 — Телец")
print("3 — Близнецы")
print("4 — Рак")
print("5 — Лев")
print("6 — Дева")
print("7 — Весы")
print("8 — Скорпион")
print("9 — Стрелец")
print("10 — Козерог")
print("11 — Водолей")
print("12 — Рыбы")

# Спрашиваем у пользователя про его знак
zodiac = int(input("{blue}Введите число с номером знака зодиака: {endcolor}".format(blue="\033[96m",
                                                                                    endcolor="\033[0m")))

# Если число введено верно — выдаём гороскоп
if 0 < zodiac < 13:
    print(random.choice(first) + "\n" + random.choice(second), random.choice(second_add)+"\n" + random.choice(third))
else:
    print("Вы ошиблись с числом, запустите программу ещё раз")
