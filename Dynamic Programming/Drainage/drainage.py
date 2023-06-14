


def dynamic(jess, x ,y):
    global list2
    global dp
    abc = 1

    if solved[x][y]:
        return dp[x][y]
    else:
        if (0 <= x) and (x < len(jess)) and (0 <= y) and (y < len(jess[0])):
            #print(jess[x][y+1])
            #print(jess)
            if (0 <= x < len(jess)-1) and jess[x][y] < jess[x+1][y]:
                abc = max(abc, 1 + dynamic(jess, x+1, y))

            if (0 <= y) and (y < len(jess[0])-1) and jess[x][y] < jess[x][y+1]:
                abc = max(abc, 1 + dynamic(jess, x, y+1))

            if (0 <= x) and (x < len(jess)+1) and jess[x][y] < jess[x-1][y]:
                abc = max(abc, 1 + dynamic(jess, x-1, y))

            if (0 <= y) and (y < len(jess[0])+1) and jess[x][y] < jess[x][y-1]:
                abc = max(abc, 1 + dynamic(jess, x, y-1))

            solved[x][y] = True
            dp[x][y] = abc

        return abc


if __name__ == "__main__":
    # global jess
    global list1
    global list2
    global dp
    x = int(input())
    for i in range(x):
        x1,x2,x3 = input().split()
        x2 = int(x2)
        x3 = int(x3)
        #jess = [[0 for _ in range(x3)] for _ in range(x2)]
        jess = []


        y = 0
        solved = [[False for _ in range(x3)] for _ in range(x2)]
        dp = [[0 for _ in range(x3)] for _ in range(x2)]
        for i in range(x2):
            y = input().split()
            jess.append(y)
            #solved.append(y)

        for i in range(len(jess)):
            for j in range(len(jess[i])):
                jess[i][j] = int(jess[i][j])
                #solved[i][j] = int(solved[i][j])

        #print(jess,jess[0], jess[1])
        list2 = []
        list1 = []
        hi = 0
        max_index = 0

        for i in range(len(jess)):
            for j in range(len(jess[i])):
                if dynamic(jess, i, j) > hi:

                    hi = dynamic(jess, i, j)
                    max_index = jess[i][j]
        #print(jess)
        list2.append(max_index)
        list1.append(hi)
        list1 = sorted(list1)

        #print(list1)
        #print(list2)
        #print(solved)
        print(str(x1)+":"+" "+str(list1[0]))


