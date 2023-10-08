def task_1():
    with open("F1.txt", "w", encoding="UTF-8") as file_F1:
        print("Увядзіце радкі з дадзенымі праз Enter:")
        while True:
            info = input()
            if info == "":
                break
            print(info, file=file_F1)

    with open ("F1.txt", "r", encoding="UTF-8") as file_F1, open ("F2.txt", "w", encoding="UTF-8") as file_F2:
        for line in file_F1:
            if line.rstrip().endswith("A"):
                print(line.rstrip(), file=file_F2)