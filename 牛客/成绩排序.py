import sys

for line in sys.stdin:
    msg = ""
    for i in range(int(line.replace("\n",""))+1):
        msg += input()+"\n"

    msgs = msg.split("\n")
    reverse = int(msgs[0])
    students = msgs[1: ]

    slist = []
    for student in students:
        if len(student)<1:
            continue
        t = student.split(" ")

        slist.append((t[0],int(t[1])))
    slist.sort(key=lambda x:x[1],reverse=True if reverse == 0 else False)

    string = ""
    for i in slist:
        string += i[0]+" "+str(i[1]) + "\n"
    print(string)

