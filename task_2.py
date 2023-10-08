def ev_score():
    last_name = {"low": [], "ave": [], "hight": []}
    with open("average_score.txt", "r", encoding="UTF-8") as file_ev:
        for line in file_ev:
            if float(line.rstrip().split()[1]) > 4 and float(line.rstrip().split()[1]) <= 6:
                last_name["low"].append(line.rstrip().split()[0])
            elif float(line.rstrip().split()[1]) > 6 and float(line.rstrip().split()[1]) <= 8:
                last_name["ave"].append(line.rstrip().split()[0])
            else:
                last_name["hight"].append(line.rstrip().split()[0])

        print("\nСтудэнты з балам ад 4 да 6:", *last_name["low"], sep="\n")
        print("\nСтудэнты з балам ад 6 да 8:", *last_name["ave"], sep="\n")
        print("\nСтудэнты з балам больш за 8:", *last_name["hight"], sep="\n")
        print("\nСтудэнт з самым высокім сярэднім балам:", max(last_name["hight"]))