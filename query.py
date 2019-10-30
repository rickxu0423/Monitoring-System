import sys, glob, os, time, datetime

def check(query):
    if len(query) < 6:
        print("missing input")
        return False
    if query[1] != "0" and query[1] != "1":
        print("wrong cpu_id")
        return False
    if len(query[3]) != 5 or len(query[5]) != 5:
        print("wrong hour-minute")
        return False
    if len(query[2]) != 10 or len(query[4]) != 10:
        print("wrong year-month-day")
        return False
    return True

while 1:
    if len(sys.argv) < 2:
        folder = input("Enter a folder name: ") 
        if folder:
            if os.path.exists(folder):
                os.chdir(folder)
                break
            else:
                print("Folder not exists!")
    else:
        folder = sys.argv[1]
        if os.path.exists(folder):
                os.chdir(folder)
                break
        else:
            print("Folder not exists!")
            exit()


queryTable = dict()
print("Initializing query tool...")
for file in glob.glob("*.log"):
    f = open(file)
    for line in f:
        if not line:
            continue
        else:
            L = line.strip().split("-")
            if L[0] in queryTable:
                if L[1] in queryTable[L[0]]:
                    queryTable[L[0]][L[1]][L[2]] = L[3]
                else:
                    queryTable[L[0]][L[1]] = {L[2]:L[3]} 
            else:
                queryTable[L[0]] = {L[1]:{L[2]:L[3]}}
    #print(queryTable)

while 1:
    query = input("QUERY: ")
    queryList = query.split(" ")
    if query == "exit":
        break
    elif not check(queryList):
        print("Input-type error")
    else:       
        IP = queryList[0]
        cpu_id = queryList[1]
        temList_1 = queryList[2].split("-") + queryList[3].split(":")
        temList_2 = queryList[4].split("-") + queryList[5].split(":")
        for i in range(len(temList_1)):
            temList_1[i] = int(temList_1[i])
            temList_2[i] = int(temList_2[i])
        dateTime = datetime.datetime(temList_1[0],temList_1[1],temList_1[2],temList_1[3],temList_1[4])
        start_time_stamp = int(dateTime.strftime("%s"))
        dateTime = datetime.datetime(temList_2[0],temList_2[1],temList_2[2],temList_2[3],temList_2[4])
        end_time_stamp = int(dateTime.strftime("%s"))
        timeCounter = start_time_stamp
        print(f"CPU{cpu_id} usage on {IP}:")
        while timeCounter < end_time_stamp:
            time = datetime.datetime.fromtimestamp(timeCounter)
            try:
                print(time, queryTable[str(timeCounter)][IP][cpu_id])
            except:
                print("Can't find any records")
            timeCounter += 60
