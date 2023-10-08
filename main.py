import task_1
import task_2
import task_3
import task_4


def menu():
    print("Меню праграмы:\n"
          "1. Заданне на запіс дадзеных у файл F1 і капіраванне іх у файл F2\n"
          "2. Заданне з студэнтамі і іх сярэднім балам\n"
          "3. Заданне з прадметамі і іх працягласцю\n"
          "4. Заданне заданне на выручку камапаній і json файл.\n"
          "Любы іншы лік - Выхад з праграмы.\n")
    while True:
        try:
            var = int(input("Увядзіце патрэюны вам варыянт: "))
            break
        except ValueError:
            print("Вы ўвялі не лік.\nПаспрабуйце яшчэ раз.")
    return var


while True:
    var = menu()

    match(var):
        case 1:
            task_1.task_1()
        case 2:
            task_2.ev_score()
        case 3:
            task_3.subj_hours()
        case 4:
            task_4.companies()
        case _:
            print("Да пабачэння")
            exit()