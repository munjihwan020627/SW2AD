def Get_Score(j, a, b, c, d, e):        #j는 add버튼을 눌렀을때의 resultbox의 keyindex예정
    cnt = 0
    lst = [a, b, c, d, e]
    if j<6:
        for i in lst:
            if j+1 == i:
                cnt += i

    elif j == 6:
        for i in lst:
            cnt+=i

    elif j == 7:
        if len(set(lst)) == 2:
            lst.sort()
            for i in lst:
                if lst[0] != lst[1] ^ lst[3] != lst[4]:
                    cnt+=i

    elif j == 8:
        if len(set(lst)) == 2:
             lst.sort()
             if lst[1] != lst[2] ^ lst[2] != lst[3]:
                cnt += 25

    elif j == 9:
        if [1,2,3,4] or [2,3,4,5] or [3,4,5,6] in sorted(list(set(lst))):
            cnt += 30

    elif j == 10:
        a = sorted(lst)
        if a == [1,2,3,4,5] or a==[2,3,4,5,6]:
            cnt +=40

    elif j == 11:
        if len(set(lst)) == 1:
            cnt+=50

    print(cnt)

    return cnt
