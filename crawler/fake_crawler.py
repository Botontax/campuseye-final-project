import random

def get_event_reason():
    reasons = [
        "普通上課",
        "期中考週",
        "社團活動",
        "專題討論",
        "空堂時間",
        "校園活動影響"
    ]
    return random.choice(reasons)