def scorecalc(dice, text):
    s = 0
    if text == "Aces":
        for i in range(5):
            if dice[i] == 1:
                s += dice[i]
        return s
    elif text == "Deuces":
        for i in range(5):
            if dice[i] == 2:
                s += dice[i]
        return s
    elif text == "Threes":
        for i in range(5):
            if dice[i] == 3:
                s += dice[i]
        return s
    elif text == "Fours":
        for i in range(5):
            if dice[i] == 4:
                s += dice[i]
        return s
    elif text == "Fives":
        for i in range(5):
            if dice[i] == 5:
                s += dice[i]
        return s
    elif text == "Sixes":
        for i in range(5):
            if dice[i] == 6:
                s += dice[i]
        return s
    elif text == "Choice":
        s = sum(dice)
        return s
    elif text == "4 of a Kind":
        same = max(dice.count(1), dice.count(2), dice.count(3), dice.count(4), dice.count(5), dice.count(6))
        if same >= 4:
            s = sum(dice)
        return s
    elif text == "Full House":
        same1 = max(dice.count(1), dice.count(2), dice.count(3), dice.count(4), dice.count(5), dice.count(6))
        same2 = 1
        for i in range(1, 7):
            if 1 < dice.count(i) < same1:
                same2 = dice.count(i)
        if (same1 == 3 and same2 == 2) or same1 == 5:
            s = sum(dice)
        return s
    elif text == "S. Straight":
        myset = set(dice)
        lst = [x for x in myset]
        lst.sort()
        for i in range(len(lst)):
            lst[i] = lst[i] - i
        seq = max(lst.count(1), lst.count(2), lst.count(3))
        if seq >= 4:
            s = 15
        return s
    elif text == "L. Straight":
        myset = set(dice)
        lst = [x for x in myset]
        lst.sort()
        for i in range(len(lst)):
            lst[i] = lst[i] - i
        seq = max(lst.count(1), lst.count(2))
        if seq == 5:
            s = 30
        return s
    elif text == "Yacht":
        same = max(dice.count(1), dice.count(2), dice.count(3), dice.count(4), dice.count(5), dice.count(6))
        if same == 5:
            s = 50
        return s
    return 0