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


table = ["\n", 0, 1, 1, 0, "\n", 1, 0, 1, 1, "\n", 1, 1, 0, 1, "\n", 1, 1, 1, 1, "\n", 0, 1, 1, 0]
print(*table)


coins = (num_q, num_d)


def game(p: tuple, e=0):  # step 2: choose a turn
    # figure out how to restart
    quarter, dime = p  # split the tuple
    # index = coord_.index((quarter, dime))
    # state = table[index]
    counter = 0
    print(f"------\nquarters: {quarter}, dimes: {dime}")
    if dime >= 0 and quarter >= 0:  # state; not (0,0)
        turn = e  # represent whose turn it is
        if turn == 0:
            i = input("dimes or quarters: ")  # choice
            if "dime" in i or "d" in i:
                d = input("How many do you want to take?:  ")
                if "1" in d and dime - 1 >= 0:  # taking the dimes
                    dime -= 1
                elif "2" in d and dime - 2 >= 0:
                    dime -= 2
                else:  # restart function
                    print("this not allowed, go again \n")
                    return game((quarter, dime), turn)
            elif "quarter" in i or "q" in i:  # taking the quarters
                q = input("How many do you want to take?:  ")
                if "1" in q and quarter - 1 >= 0:  # taking the dimes
                    quarter -= 1
                elif "2" in q and quarter - 2 >= 0:
                    quarter -= 2
                elif "3" in q and quarter - 3 >= 0:
                    quarter -= 3
                else:  # restart function
                    print("this not allowed, go again \n")
                    return game((quarter, dime), turn)
            else:  # restart
                print("this not allowed, go again \n")
                return game((quarter, dime), turn)
            if (quarter, dime) == (0, 0):  # you take the last one, you win
                print((quarter, dime))
                return "You Win"
            turn = 1
        print((quarter, dime))
        if turn == 1:
            print("AI turn: ")
            choice = 3  # how much to take
            action = 0
            while choice > 0:  # (1,1)
                if (quarter - choice) >= 0 or (dime - choice) >= 0:  # 3 -> x, 2 -> x, 1 -> v
                    if quarter - choice >= 0:  # 1 -> v
                        wtv = coord_.index((quarter - choice, dime))  # quarters (0,1)
                        if table[wtv] == 0:  # winning state on taking quarter (0,1) = 1
                            quarter -= choice
                            action = 1
                            break
                    if choice <= 2:  # dimes
                        if dime - choice >= 0:
                            nice = coord_.index((quarter, dime - choice))

                            if table[nice] == 0:  # winning state on taking dimes
                                dime -= choice
                                action = 1
                                break
                    choice -= 1
                # if taking neither makes winning, take one less

                elif quarter - choice < 0 or dime - choice < 0:  # lose_state = 2
                    choice -= 1
            if action == 0:
                if quarter - 1 >= 0:
                    quarter -= 1
                elif dime - 1 >= 0:
                    dime -= 1
            if (quarter, dime) == (0, 0):  # if AI takes the last one, you lose
                return "You Lose"
            turn = 0
        print((quarter, dime))
        return game((quarter, dime), turn)


print(game(coins, 1))
