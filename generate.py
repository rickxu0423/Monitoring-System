from server import Server
import sys, os, logging, time, datetime


def incrementIP(IP):
    IP_row = IP.split(".")
    if int(IP_row[len(IP_row) - 2]) > 255 and int(IP_row[len(IP_row) - 1]) > 255:
        print("Server Overflow")
        return IP
    if int(IP_row[len(IP_row) - 1]) < 255:
        IP_row[len(IP_row) - 1] = str(int(IP_row[len(IP_row) - 1]) + 1)
    else:
        IP_row[len(IP_row) - 1] = "0"
        IP_row[len(IP_row) - 2] = str(int(IP_row[len(IP_row) - 2]) + 1)
    return IP_row[0] + "." + IP_row[1] + "." + IP_row[2] + "." + IP_row[3]

def incrementTime(time):
    if time[1] < 59:
        time[1] += 1
    else:
        time[1] = 0
        time[0] += 1
    return time

while 1:
    if len(sys.argv) < 2:
        folder = input("Enter a folder name: ") 
        if folder:
            break
    else:
        folder = sys.argv[1]
        break


if not os.path.exists(folder):
    os.mkdir(folder)

#Initialization
# Create timestamp
dateTime = datetime.datetime(2014,10,31,0,0)
unixtime = int(dateTime.strftime("%s"))
IP = "192.168.0.0"
cpu_id = "0"
usage = "0"

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
logging.getLogger().setLevel(logging.INFO)
PATH = os.path.join(folder, 'file.log')
f_handler = logging.FileHandler(PATH,"w")
logger.addHandler(f_handler)
#logger.info(f'{unixtime}-{IP}-{cpu_id}-{usage}%')

counter = 0
serverList = []
while counter < 1000:
    serverList.append(Server(IP))
    IP = incrementIP(IP)
    counter += 1

timeList = [0,0]
while timeList[0] < 24 and timeList[0] < 60:
    print(timeList)
    dateTime = datetime.datetime(2014,10,31,timeList[0],timeList[1])
    unixtime = int(dateTime.strftime("%s"))
    for server in serverList:
        returnList = server.generateLog()
        for stuff in returnList:
            IP = stuff[0]
            cpu_id = stuff[1]
            usage = stuff[2]
            logger.info(f'{unixtime}-{IP}-{cpu_id}-{usage}%')
    timeList = incrementTime(timeList)





