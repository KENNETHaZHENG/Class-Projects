# QUARTERS and DIMES
# coord_ = ["Dimes and Quarters:"]  # assume you go first; you have to take something

num_q = 4
num_d = 3


coord_ = []
for quarters in range(num_q + 1):
    coord_.append("\n")
    for dimes in range(num_d + 1):
        coord_.append((quarters, dimes))

print(*coord_)

# I have removed my classmates' work from this version
table = ["\n", 0, 1, 1, 0, "\n", 1, 0, 1, 1, "\n", 1, 1, 0, 1, "\n", 1, 1, 1, 1, "\n", 0, 1, 1, 0]
print(*table)


coins = (num_q, num_d)


def game(p: tuple, e):
    quarter, dime = p  # split the tuple

    # says the total number od quarters and dimes left:
    print(f"------\nquarters: {quarter}, dimes: {dime}")
    # ----
    if e == 0:  # player turn if e = 0
        # ----
        i = input("dimes or quarters: ")  # choosing which coin

        if "dime" in i or "d" in i:  # take dimes
            counter = 2  # can only take at max of 2
        elif "quarter" in i or "q" in i:  # taking the quarters
            counter = 3  # can take at max of 3
        else:  # restart
            print("Not a valid option, go again. \n")
            return game((quarter, dime), e)
        # ----
        t = input("How many do you want to take?:  ")  # how much to take
        # check if int(t) is good and it's less than the counter:
        if t.isdigit() and int(t) <= counter:  # checks if t has digits
            if counter == 2 and dime - int(t) >= 0:  # if dime
                dime -= int(t)
            elif counter == 3 and quarter - int(t) >= 0:  # if quarter
                quarter -= int(t)
            else:
                print("No\n")
                return game((quarter, dime), e)
        else:  # restart
            print("Not allowed, go again \n")
            return game((quarter, dime), e)
        # ----
        if (quarter, dime) == (0, 0):  # you take the last one, you win
            print((quarter, dime))
            return "You Win"
        print((quarter, dime))  # shows the aftermath
        e = 1  # switch turn
    # ----
    if e == 1:  # AI turn when e = 1
        print("\nBoB the Destroyer of the Abyss and holder of the Morning Star's turn: ")

        choice = 3  # how much to take
        action = 0  # know whether AI took something
        while choice > 0:

            # check if taking won't go into negatives:
            if (quarter - choice) >= 0 or (dime - choice) >= 0:
                if quarter - choice >= 0:  # 4 - 2
                    # ----
                    # find the index of (quarter, dime) after taking quarter
                    wtv = coord_.index((quarter - choice, dime))
                    if table[wtv] == 0:  # winning state on taking quarter
                        quarter -= choice  # take the thing
                        action = 1
                        print(f"They took {choice} quarter(s)")
                        break
                # ----
                if choice <= 2:  # dimes since we can't take 3 dimes
                    # ----
                    if dime - choice >= 0:
                        nice = coord_.index((quarter, dime - choice))
                        if table[nice] == 0:  # winning state on taking dimes
                            dime -= choice
                            action = 1
                            print(f"They took {choice} dime(s)")
                            break
                choice -= 1  # if taking neither makes winning, take one less

            elif quarter - choice < 0 or dime - choice < 0:
                choice -= 1
        # ----
        if action == 0:  # if no winning state, take a random number of quarters or dimes
            while action == 0:
                c = random.randint(1, 2)  # random number generator (RNG)
                # 1 = quarters
                if quarter != 0 and c == 1:
                    while quarter == quarter:
                        choice = random.randint(1, 3)
                        if quarter - choice >= 0:
                            quarter -= choice
                            print(f"took {choice} quarter(s)")
                            action = 1
                            break
                # ----
                elif dime != 0 and c == 2:
                    while dime == dime:
                        choice = random.randint(1, 2)
                        if dime - choice >= 0:
                            dime -= choice
                            print(f"took {choice} dime(s)")
                            action = 1
                            break
        # ----
        if (quarter, dime) == (0, 0):  # if AI takes the last one, you lose
            print((quarter, dime))
            return "You Lose"
        e = 0
    print((quarter, dime))
    return game((quarter, dime), e)  # recursive: Go again until (0,0)


print(game(coins, 1))
