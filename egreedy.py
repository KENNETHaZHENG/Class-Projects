import random

# comment what each list do and explain why

# pick an e value
# go to cafeteria for 4 days and do a random.normalvariate() on each
# record the happiness value for each as days go by ( find average )
# go to the highest mean of the cafeterias (100-e)% of the time
# e% of the time go to a random cafeteria

caf = [{"average": 7, "std_dev": 3}, {"average": 4, "std_dev": 10}, {"average": 10, "std_dev": 6},
       {"average": 5, "std_dev": 2}]  # holds the values for random.normalvariate for each cafe


def eGreedy(e=10):
    # first 4 days going to 4 cafeterias
    c1 = random.normalvariate(7, 3)
    # if we each generate a random value for each cafeteria, do each function have different values?
    c2 = random.normalvariate(4, 10)
    c3 = random.normalvariate(10, 6)
    c4 = random.normalvariate(5, 2)

    c_hap = [c1, c2, c3, c4]  # holds the total happiness of each cafe
    d_c = [1, 1, 1, 1]  # holds the number of days going to each cafeteria
    count = 5  # the fifth day

    while count <= 200:  # remaining days
        l1 = []  # holds the averages of each cafeteria
        for index in range(4):  # 0,1,2,3 <- indexes;
            # avg of all cafe; refreshes l1 each day
            a = (c_hap[index]) / (d_c[index])  # getting the avg of each cafe
            l1.append(a)  # put the avg in the list

        r = random.random()  # random num (0, 1)
        if r < (e / 100):  # choosing a random cafeteria
            i = random.randint(0, 3)
        else:
            maxi = 0
            for item in l1:  # go through each mean happiness of each cafe
                if maxi < item:  # find the highest mean
                    maxi = item  # replace old value with bigger value
            i = l1.index(maxi)  # find index of highest mean (go to which cafe)

        # adding new happiness values
        c_hap[i] += random.normalvariate(caf[i]["average"], caf[i]["std_dev"])
        # add to num of time visited
        d_c[i] = d_c[i] + 1
        count += 1  # adding the days

    t_hap = 0  # counting the total happiness in c_hap
    for i in c_hap:
        t_hap = t_hap + i
    return t_hap  # total happiness


print(eGreedy(10))
