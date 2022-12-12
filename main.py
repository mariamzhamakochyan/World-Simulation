class WorldSimulation:
    def __init__(self,time = None,  morning = None):
        self.morning = morning
        self.time = time

    def checkDay(self):
        time = input("Please enter the time: ")
        self.time = time
        x,y = time.split(":")
        if 8 <= int(x) <= 18 and 0 <= int(y) <= 59:
            self.morning = True
            print("It's morning... ")
        elif 19 <= int(x) <= 24 or 1 <= int(x) <= 7 and 00 <= int(y) <= 59:
            self.morning = False
            print("It's night zzz... ")
        else:
            print("INVALIDINPUT")

    def Status(self):
        if self.morning == True:
            print("Frog is awake...")
            
        else:
            print("Frog is sleeping...")
    
    def Eat(self):
        if self.morning == False:
            print("Frog ate and fell asleep.")
        elif self.morning == True:
            x,y = self.time.split(":")
            if int(x) % 2 == 0:
                print("Frog is eatting grass..")
            else:
                print("Frog is chilling :D")
    
    def Move(self):
        if self.morning == False:
            print("Let's assume that our frog is not sleepwalker,so at the moment is asleep and not moving:")
        else:
            print("Frog enjoys life in this wonderful world, (briefly moving)")
    
    def Breath(self):
        if self.morning == True:
            print("Frog is breating cuz its morning:")
        elif self.morning == False:
            print("Frog is not breathing. But don't worry he is alive:")
    
    def Tree(self):
        if self.morning == True:
            print("As it is morning, the sun causes photosynthesis to occur.")
        elif self.morning == False:
            print("it's night, so no more photosynthesis.")
    
    def Grass(self):
        if self.morning == False:
            print("Grass is unlimited.")
        elif self.morning == True:
            x,y = self.time.split(":")
            if int(x) % 2 == 0:
                print("The grass grows endlessly.")
            else:
                print("Grass is unlimited, the frog can eat whenever he wants")
    def Sun(self):
        print("In this world the sun shines for 10 hours and does not shine for 14 hours")
        x,y = self.time.split(":")
        if self.morning == True:
            x,y = self.time.split(":")
            minutes = (16 - int(x))*60 + int(y)
            print(f"The sun will shine for another {minutes} minutes")
        else:
            print("Its night, so the sun does not shine")

        
    
day = WorldSimulation()
day.checkDay()
day.Tree()
day.Status()
day.Eat()
day.Grass()
day.Move()
day.Breath()
day.Sun()
