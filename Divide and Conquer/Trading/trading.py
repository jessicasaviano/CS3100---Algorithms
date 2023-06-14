import math
import copy



def brute(sorting):
    min = float('inf')
    for i in range(len(sorting)):
        for j in range(i + 1, len(sorting)):
            distance = math.sqrt((sorting[j][0] - sorting[i][0]) * (sorting[j][0] - sorting[i][0]) + (
                    sorting[j][1] - sorting[i][1]) * (sorting[j][1] - sorting[i][1]))
            if distance < min:
                min = distance
    return min



def recurse(sorting):
    points = len(sorting)
    if points <= 3: #base case
        return brute(sorting)



    median = points // 2
    middle = sorting.index(sorting[median])
    sorting_l = sorting[:median]
    sorting_r = sorting[median:]
    #print(sorting_l)
    #print(sorting_r)

    delta_l = recurse(sorting_l)
    delta_r = recurse(sorting_r)
    #print(delta_l)
   #print(delta_r)

    smaller = min(delta_l, delta_r)
    #print(smaller)
    runway = []
    ex = sorting_l + sorting_r
    #print(ex)
    #print(sorting)
    for i in range(points):
        if abs(ex[i][0] - ex[middle][0]) < smaller:
            runway.append(sorting[i])
            #print(runway)


    runway = sorted(runway, key=lambda x: x[1])
    #print(runway)

    if len(runway) == 1:
        final_answer = smaller
    elif len(runway) <= 7:
        #print("hi")
        x = brute(runway)
        #print(x)
        #print(smaller)
        if x < smaller:
            final_answer = x
        else:
            final_answer = smaller
    else:
        for i in range(len(runway) - 7):
            #print('yo')
            #print(runway[i:i+7])
            jess1 = brute(runway[i:i+7])
            #print(jess1)
            #print(smaller)
            if jess1 < smaller:
                final_answer = jess1
            else:
                final_answer = smaller


    return final_answer





if __name__ == "__main__":
    x1 = float('inf')
    while x1 != 0:
        x1 = input()
        x1 = int(x1)
        if x1 == 0:
            break
        #print(x1)
        stars = [] #this while be a list of lists
        for i in range(x1):
            x,y = input().split()
            x = float(x)
            y = float(y)
            list1 = [x,y]
            stars.append(list1)
            #print(stars)
        star = sorted(stars, key=lambda x: x[0]) #INITALIZATION
        vertical = []
        for i in range(len(star)):
            vertical.append(star[i][0])

        if len(set(vertical)) == 1:
            jw = brute(star)
            if jw >= 10000:
                print("infinity")
            else:

                ans = format(jw, '.4f')
                print(ans)

        elif len(set(vertical)) != 1:
                jessica = recurse(star)

                if jessica >= 10000:
                    print("infinity")
                else:

                    ans = format(jessica, '.4f')
                    print(ans)


        stars.clear()
        star.clear()
        x = 0
        y = 0
        x1 = float('inf')
        list1 = []


