import random

class Server:
    def __init__(self, IP):
        self.IP = IP
        self.cpu_1 = "0"
        self.cpu_2 = "1"
        self.usage_1 = str(random.randint(1,101))
        self.usage_2 = str(random.randint(1,101))

    def __str__(self):
        return self.IP

    def generateLog(self):
        self.usage_1 = str(random.randint(1,101))
        self.usage_2 = str(random.randint(1,101))
        return [[self.IP, self.cpu_1, self.usage_1], [self.IP, self.cpu_2, self.usage_2]]
    
        