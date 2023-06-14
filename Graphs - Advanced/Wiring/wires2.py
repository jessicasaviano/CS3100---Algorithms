
def isjess(x):
    if x == "b":
        return True
    if x == "o":
        return True
    if x == "j":
        return True
    return False

def isjessswitch(y):
    if y == "b":
        return True
    if y == "o":
        return True
    if y == "j":
        return True
    if y == "s":
        return True
    return False


def islight(z):
    if z == "l":
        return True
    return False

def isswitch(z):
    if z == "s":
        return True
    return False

def find(n, parent):
    # print(n)
    # print(parent[n])
    if parent[n] == n:
        return n
    return find(parent[n], parent)

def union(j, s, parent, rank):
    # print("PARENT: "+ str(find(j)))
    xroot = find(j, parent)
    yroot = find(s, parent)
    #print(xroot)
    #print(yroot)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
def firstk():
    global answer
    global parent
    global rank
    sorting = []
    parent = []
    rank = []
    for i in range(len(adjM)):
        parent.append(i)
        rank.append(0)
    #print("this: " + list(name.keys())[0][0])
    #print(name)
    for i in range(len(adjM)):
        for j in range(len(adjM[i])):
            if adjM[i][j] != 0 and isjess((list(name.keys())[i][0])) and isjess((list(name.keys())[j][0])):
                x = name[(list(name.keys()))[i]]

                y = name[(list(name.keys()))[j]]
                z = adjM[i][j]
                sorting.append([x, y, z])

    sorting = sorted(sorting, key=lambda x: x[2])
    answer = 0
    zero_edges = 0
    #print(sorting)
    #print(sorting[0][0])
    # print(parent)
    #rank = [0] * (len(sorting))
    k = 0
    zero = 0
    #print(x1 - 1)
    #while zero < len(sorting) - 1:
    for k in range(len(sorting)):
        #print("this is zero")
        x = sorting[k][0]
        y = sorting[k][1]
        z = sorting[k][2]
        # print("x: " + str(x))
        # print("y: " + str(y))
        # print("y: " + str(z))
        # print("x: " + str(parent[y]))
        if find(x, parent) != find(y, parent):
            zero += 1
            answer += z
            union(x, y, parent, rank)

        if zero == len(sorting) - 1:
            break

    return answer

    #---SECOND KRUSK_____
def secondk():
    global new_answer
    new_sorting = []

    for i in range(len(adjM)):
        for j in range(len(adjM[i])):
            if adjM[i][j] != 0 and isjessswitch((list(name.keys())[i][0])) and isjessswitch((list(name.keys())[j][0])):
                if isswitch((list(name.keys())[i][0])) and isswitch((list(name.keys())[j][0])):
                    continue
                else:

                    x = name[(list(name.keys()))[i]]

                    y = name[(list(name.keys()))[j]]
                    z = adjM[i][j]
                    new_sorting.append([x, y, z])

    new_sorting = sorted(new_sorting, key=lambda x: x[2])
    new_answer = 0
    zero_edges = 0
    #print(sorting)
    #print(sorting[0][0])
    # print(parent)
    new_rank = [0] * (1000000)
    k = 0
    zero = 0
    #print(x1 - 1)
    #while zero < len(sorting) - 1:
    for k in range(len(new_sorting)):
        #print("this is zero")
        x = new_sorting[k][0]
        y = new_sorting[k][1]
        z = new_sorting[k][2]
        # print("x: " + str(x))
        # print("y: " + str(y))
        # print("y: " + str(z))
        # print("x: " + str(parent[y]))
        if find(x, parent) != find(y, parent):
            zero += 1
            new_answer += z
            union(x, y, parent, rank)

        if zero == len(new_sorting) - 1:
            break

    return new_answer

def thirdk():    #----THIRD K-----
    global t_answer
    jesssav = 0
    t_sorting = []
    for i in range(len(adjM)):
        for j in range(len(adjM[i])):
            if adjM[i][j] != 0:
                if islight((list(name.keys())[i][0])) and islight((list(name.keys())[j][0])):
                    if lights[list(name.keys())[i]] == lights[list(name.keys())[j]]:
                        #print(lights[list(name.keys())[i]])
                        x = name[(list(name.keys()))[i]]

                        y = name[(list(name.keys()))[j]]
                        z = adjM[i][j]
                        t_sorting.append([x, y, z])

                elif isswitch((list(name.keys())[i][0])) and islight((list(name.keys())[j][0])):
                    if lights[list(name.keys())[j]] == list(name.keys())[i]:
                        #print("yo")
                        x = name[(list(name.keys()))[i]]

                        y = name[(list(name.keys()))[j]]
                        z = adjM[i][j]
                        t_sorting.append([x, y, z])

                elif isswitch((list(name.keys())[j][0])) and islight((list(name.keys())[i][0])):
                    if lights[list(name.keys())[i]] == list(name.keys())[j]:
                        x = name[(list(name.keys()))[i]]

                        y = name[(list(name.keys()))[j]]
                        z = adjM[i][j]
                        t_sorting.append([x, y, z])

                elif isswitch((list(name.keys())[j][0])) and isswitch((list(name.keys())[i][0])):

                    continue

    t_sorting = sorted(t_sorting, key=lambda x: x[2])
    #print(t_sorting)
    t_answer = 0
    zero_edges = 0

    t_rank = [0] * (10000000)
    k = 0
    zero = 0

    for k in range(len(t_sorting)):
        #print("this is zero")
        x = t_sorting[k][0]
        y = t_sorting[k][1]
        z = t_sorting[k][2]

        if find(x, parent) != find(y, parent):
            zero += 1
            t_answer += z
            union(x, y, parent, rank)

        if zero == len(t_sorting):
            break

    return t_answer








if __name__ == "__main__":

    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    name = {}
    lights = {}
    number = 0
    curSwitch = ""
    for i in range(x1):
        s1, s2 = input().split()
        name[s1] = number
        number += 1
        if s2 == "switch":
            curSwitch = s1
        elif s2 == "light":
            lights[s1] = curSwitch

    j1 = len(name.keys())
    #print(lights)
    # print(name)
    # print(j1)
    adjM = [[0 for _ in range(j1)] for _ in range(j1)]
    # print(adjM)
    # print(type((list(name.keys())[0][0])))
    for i in range(x2):
        q1, q2, q3 = input().split()
        y1 = name[q1]
        y2 = name[q2]
        if q3 != 0:
            q3 = int(q3)
            adjM[y1][y2] = q3
            adjM[y2][y1] = q3



    #print(adjM)
    #print(fristkruals(0 + hgdbfvjhnd)
    firstk()
    a = int(answer)
    secondk()
    b = int(new_answer)
    thirdk()
    c = int(t_answer)
    result = a+b+c
    print(result)
















