import sys, glob, os, time, datetime

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
    if query == "exit":
        break
    else:
        queryList = query.split(" ")
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
            print(time, queryTable[str(timeCounter)][IP][cpu_id])
            timeCounter += 60
