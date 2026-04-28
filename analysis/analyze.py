def analyze_people(count):
    if count < 5:
        return "偏少"
    elif count < 15:
        return "普通"
    else:
        return "擁擠"