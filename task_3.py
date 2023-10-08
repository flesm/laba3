def subj_hours():
    with open("class.txt", "r", encoding="UTF-8") as file_class:
        subjects = {}
        for line in file_class:
            subject, hours = line.strip().split(": ")
            hours = hours.split()
            total_hours = sum(int(hour.split("(")[0]) for hour in hours)
            subjects[subject] = total_hours
        print(subjects)