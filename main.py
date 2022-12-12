time = input("Please enter the time: ")
x,y = time.split(":")
current_time = x
cur = y

class Day:
    def __init__(self):
        pass
    def morning(self):
        if 19 >= int(current_time) >= 8:
            return True
        return False

class Frog:
    def __init__(self):
        pass
    
    def Status(self):
        if day.morning():
            return("Frog is awake...")
        return ("Frog is sleeping...")
    
    def Breath(self):
        if day.morning():
            return("Frog is breating cuz its morning:")
        else:
            return("Frog is not breathing. But don't worry he is alive:")
    
    def Eat(self):
        if not day.morning():
            return("Frog ate and fell asleep.")
        elif day.morning():
            if int(current_time) % 2 == 0:
                return("Frog is eatting grass..")
            else:
                return("Frog is chilling :D")
    
    def Move(self):
        if not day.morning():
            return("Let's assume that our frog is not sleepwalker,so at the moment is asleep and not moving:")
        else:
            return("Frog enjoys life in this wonderful world, (briefly moving)")


class Tree:
    def __init__(self):
        pass
    
    def tree_(self):
        if day.morning():
            return("As it is morning, the sun causes photosynthesis to occur.")
        else:
            return("it's night, so no more photosynthesis.")

class Grass:
    def __init__(self):
        pass
    
    def grass_(self):
        if not day.morning():
            print("Grass is unlimited.")
        elif day.morning():
            if int(current_time) % 2 == 0:
                return("The grass grows endlessly.")
            else:
                return("Grass is unlimited, the frog can eat whenever he wants")

class Sun:
    def __init__(self):
        pass
    def sun_(self):
        # In this world the sun shines for 10 hours and does not shine for 14 hours
        if day.morning():
            minutes = (16 - int(current_time))*60 + int(cur)
            return(f"The sun will shine for another {minutes} minutes")
        else:
            return("Its night, so the sun does not shine")
    


day = Day()
tree = Tree()  
frog = Frog()
sun = Sun()
grass = Grass()



print(frog.Status())
print(frog.Eat())
print(frog.Breath())
print(frog.Move())
print(tree.tree_())
print(sun.sun_())
print(grass.grass_())
