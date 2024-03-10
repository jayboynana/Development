# 未ac

s = input()
e = input()
c = 0

if s[:4] == e[:4]:
    if s[4:6] == e[4:6]:
        for d in range(int(s[6:]),int(e[6:])+1):
            temp = ''
            if d < 10:
                temp = s[:6] + '0' + str(d)
            else:
                temp = s[:6] + str(d)
            if temp[::-1] == temp:
                c += 1
    else:
        for m in range(int(s[4:6]),int(e[4:6])):
            temp = ''
            if m in [1,3,5,7,8,10,12]:
                if m < 10:
                    temp = s[:4] + '0' + str(m)
                else:
                    temp = s[:4] + str(m)
                for d in range(int(s[6:]),32):
                    if d < 10:
                        temp_ = temp + '0' + str(d)
                    else:
                        temp_ = temp + str(d)
                    if temp_[::-1] == temp_:
                        c += 1
            elif m in [4,6,9,11]:
                if m < 10:
                    temp = s[:4] + '0' + str(m)
                else:
                    temp = s[:4] + str(m)
                for d in range(int(s[6:]),31):
                    if d < 10:
                        temp_ = temp + '0' + str(d)
                    else:
                        temp_ = temp + str(d)
                    if temp_[::-1] == temp_:
                        c += 1
            else:
                if int(s[:4]) % 400 == 0 or (int(s[:4]) % 4 == 0 and int(s[:4]) % 100 != 0):
                    for d in range(int(s[6:]),30):
                        temp = s[:4] + '0' + str(m)
                        if d < 10:
                            temp_ = temp+'0'+str(d)
                        else:
                            temp_ = temp + str(d)
                        if temp_[::-1] == temp_:
                            c += 1
                else:
                    for d in range(int(s[6:]),29):
                        temp = s[:4] + '0' + str(m)
                        if d < 10:
                            temp_ = temp+'0'+str(d)
                        else:
                            temp_ = temp + str(d)
                        if temp_[::-1] == temp_:
                            c += 1
        temp = e[:6]
        for d in range(1,int(e[6:])):
            if d < 10:
                temp_ = temp + '0' + str(d)
            else:
                temp_ = temp + str(d)
            if temp_[::-1] == temp_:
                c += 1

else:
    if int(s[4:6]) in [1, 3, 5, 7, 8, 10, 12]:
        for d in range(int(s[6:]), 32):
            temp = s[:6]
            if d <10 :
                temp_ = temp + '0' + str(d)
            else:
                temp_ = temp + str(d)
            if temp_[::-1] == temp_:
                c += 1
    elif int(s[4:6]) in [4, 6, 9, 11]:
        for d in range(int(s[6:]), 31):
            temp = s[:6]
            if d <10 :
                temp_ = temp + '0' + str(d)
            else:
                temp_ = temp + str(d)
            if temp_[::-1] == temp_:
                c += 1
    else:
        if int(s[:4]) % 400 == 0 or (int(s[:4]) % 4 == 0 and int(s[:4]) % 100 != 0):
            for d in range(int(s[6:]), 30):
                temp = s[:6]
                if d < 10:
                    temp_ = temp + '0' + str(d)
                else:
                    temp_ = temp + str(d)
                if temp_[::-1] == temp_:
                    c += 1
        else:
            for d in range(int(s[6:]), 29):
                temp = s[:6]
                if d < 10:
                    temp_ = temp + '0' + str(d)
                else:
                    temp_ = temp + str(d)
                if temp_[::-1] == temp_:
                    c += 1
    for m in range(int(s[4:6])+1,13):
        temp = s[:4]
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if m < 10:
                temp = temp + '0' + str(m)
            else:
                temp = temp + str(m)
            for d in range(int(s[6:]), 32):
                temp_ = temp
                if d < 10:
                    temp_ += '0' + str(d)
                else:
                    temp_ += str(d)
                if temp_[::-1] == temp_:
                    c += 1
        elif m in [4, 6, 9, 11]:
            if m < 10:
                temp = temp + '0' + str(m)
            else:
                temp = temp + str(m)
            for d in range(1, 31):
                temp_ = temp
                if d < 10:
                    temp_ += '0' + str(d)
                else:
                    temp_ += str(d)
                if temp_[::-1] == temp_:
                    c += 1
        else:
            if int(s[:4]) % 400 == 0 or (int(s[:4]) % 4 == 0 and int(s[:4]) % 100 != 0):
                for d in range(1, 30):
                    temp = str(s[:4]) + str(m)
                    if d < 10:
                        temp_ = temp + '0' + str(d)
                    else:
                        temp_ = temp + str(d)
                    if temp_[::-1] == temp_:
                        c += 1
            else:
                for d in range(1, 29):
                    temp = str(s[:4]) + str(m)
                    if d < 10:
                        temp_ = temp + '0' + str(d)
                    else:
                        temp_ = temp + str(d)
                    if temp_[::-1] == temp_:
                        c += 1
    for y in range(int(s[:4])+1,int(e[:4])):
        for m in range(1,13):
            if m in [1,3,5,7,8,10,12]:
                if m < 10:
                    temp = str(y) + '0' + str(m)
                else:
                    temp = str(y) + str(m)
                for d in range(1,32):
                    temp_ = temp
                    if d < 10:
                        temp_ += '0'+str(d)
                    else:
                        temp_ += str(d)
                    if temp_[::-1] == temp_:
                        c += 1
            elif m in [4,6,9,11]:
                if m < 10:
                    temp = str(y) + '0' + str(m)
                else:
                    temp = str(y) + str(m)
                for d in range(int(1),31):
                    temp_ = temp
                    if d < 10:
                        temp_ += '0'+str(d)
                    else:
                        temp_ += str(d)
                    if temp_[::-1] == temp_:
                        c += 1
            else:
                if int(y) % 400 == 0 or (int(y) % 4 == 0 and int(y) % 100 != 0):
                    for d in range(1, 30):
                        temp = str(y) + str(m)
                        if d < 10:
                            temp_ = temp+'0'+str(d)
                        else:
                            temp_ = temp + str(d)
                        if temp_[::-1] == temp_:
                            c += 1
                else:
                    for d in range(1,29):
                        temp = str(y) + str(m)
                        if d < 10:
                            temp_ = temp+'0'+str(d)
                        else:
                            temp_ = temp + str(d)
                        if temp_[::-1] == temp_:
                            c += 1
    for m in range(1,int(e[4:6])):
        temp = e[:4]
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if m < 10:
                temp += '0' + str(m)
            else:
                temp += str(m)
            for d in range(1,32):
                if d <10:
                    temp_ = temp + '0' + str(d)
                else:
                    temp_ = temp +str(d)
                if temp_[::-1] == temp_:
                    c += 1
        elif m in [4,6,9,11]:
            if m < 10:
                temp += '0' + str(m)
            else:
                temp += str(m)
            for d in range(1,31):
                if d <10:
                    temp_ = temp + '0' + str(d)
                else:
                    temp_ = temp +str(d)
                if temp_[::-1] == temp_:
                    c += 1
        else:
            if int(temp) % 400 == 0 or (int(temp) % 4 == 0 and int(temp) % 100 != 0):
                for d in range(1, 30):
                    temp = e[:4] + '0' + str(m)
                    if d < 10:
                        temp_ = temp + '0' + str(d)
                    else:
                        temp_ = temp + str(d)
                    if temp_[::-1] == temp_:
                        c += 1
            else:
                for d in range(1, 29):
                    temp = e[:4] + '0' + str(m)
                    if d < 10:
                        temp_ = temp + '0' + str(d)
                    else:
                        temp_ = temp + str(d)
                    if temp_[::-1] == temp_:
                        c += 1
    for d in range(1,int(e[6:])+1):
        temp = e[:6]
        if d < 10:
            temp_ = temp + '0' + str(d)
        else:
            temp_ = temp + str(d)
        if temp_[::-1] == temp_:
            c += 1
print(c)