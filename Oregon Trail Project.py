import random

months_with_31 = [1, 3, 5, 7, 8, 10, 12]

locations = ['Independence, Missouri', 'Oregon City, Oregon']

running = True

def dysentary():
    global health
    print("You have contracted dysentary, you lose some health")
    health -= random.randint(1, 2)

def broken_wheel():
    global food
    print("You hit a rock and your wheel rolled off...")
    days = random.randint(10, 14)
    print(f"Your wheel took {days} days to replace")
    food -= 3*days

def raid_by_bandits():
    global food
    food_stolen = random.randint(50, 100)
    print(f"While you were traveling, you were raided by bandits, and they stole {food_stolen} pieces of food")
    food -= food_stolen
    

while running:
    current_day = 1

    current_month = 3

    distance_left = 2000

    health = 5

    food = 500

    events = ['dysentary', 'broken wheel', 'raided by bandits']

   

    def add_day(x):
        global current_day
        global current_month
        global food
        global health
        global events

        if current_month in months_with_31:   
            if 31 - current_day >= x:   
                current_day += x
            elif 31 - current_day < x:
                current_month += 1
                current_day = current_day - 31 + x 
                health -= 2
                if random.randint(1, 10) < 2:
                    dysentary()
                elif random.randint(1, 10) < 2:
                    broken_wheel()
                elif random.randint(1, 10) < 2:
                    raid_by_bandits()
        else:   
            if 30 - current_day >= x:   
                current_day += x
            elif 30 - current_day < x:  
                current_month += 1
                current_day = current_day - 30 + x
                health -= 2
                if random.randint(1, 10) < 2:
                    dysentary()
                if random.randint(1, 10) < 2:
                    broken_wheel()
                if random.randint(1, 10) < 2:
                    raid_by_bandits()
            
    def travel():
        global distance_left
        global food
        distance_left -= random.randint(30, 60)
        days = random.randint(3, 7)
        add_day(days)
        print("Whew, I'm tired!")
        food -= 5*days
    def rest():
        global health
        global current_day
        global food
        if health < 5:
            health += 1
        else:
            print("Crap, this was a waste of time...")
        days = random.randint(2, 5)
        add_day(days)
        food -= 3*days
        print("Wow, sure is nice to relax!")

    def hunt():
        global food
        global current_day
        food += 100
        days = random.randint(2, 5)
        add_day(days)
        food -= 4*days
        print("PEW PEW PEW")

    def status():
        print(f"{pName}'s Stats: food: {food}lbs, health: {health}, distance traveled: {2000 - distance_left} miles, day: {current_month}/{current_day}")

    def help():
        print("You can type in any of the following commands: travel, rest, hunt, status, help, quit")

    input("press ENTER to start")

    pName = input("What is your name?: ")

    print("Welcome to the Oregon Trail! Your goal is to travel from Independence, Missouri, all the way to Oregon City, Oregon! You will start with 500lbs of food and 5 lives. Good luck!")

    while True:
        print("")
        turn = input("What would you like to do? travel, rest, hunt, status, help, quit: ")

        """while turn != 'travel'or 'rest' or 'hunt' or 'status' or 'help' or 'quit':
            turn = input("What would you like to do? travel, rest, hunt, status, help, quit: ")"""

        if turn == 'travel':
            travel()
            if distance_left <= 0:
                print("You have successfully reached Oregon City, Oregon!")
                break
            else:
                print(f"You have {distance_left} miles left to travel")
        elif turn == 'rest':
            rest()
        elif turn == 'hunt':
            hunt()
        elif turn == 'status':
            status()
        elif turn == 'help':
            help()
        elif turn == 'quit':
            break
        if current_month == 13:
            print("You did not reach Oregon before December 31st, you die now")
            break
        
        if health < 1:
            print("You ran out of lives, now you are dead...")
            break

        if food < 1:
            print("You ran out of food, you starved to death :(")
            break