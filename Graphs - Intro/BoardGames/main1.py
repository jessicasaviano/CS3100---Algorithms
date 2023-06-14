def paths(v, dist, happened, way):
    # print("hii")

    happened[v] = True
    way.append(v)
    # print("im here")
    # print(v)
    if v == dist:
        #print(way)
        print(*way, sep='-')

    else:
        for g in range(len(adjM)):
            # print("hiii")
            #for f in adjM[g]:
            if adjM[v][g] == 1 and happened[g] is False:
                    #print(happened[g])
                paths(g, dist, happened, way)

    way.pop()
    happened[v] = False


if __name__ == "__main__":
    x1 = input()
    x2 = input()
    x1 = int(x1)
    x2 = int(x2)
    # print(x1)
    # print(x2)
    graph = {}
    x1_list = []
    adjM = []
    for i in range(x1):
        x1_list.append(i)
        x1_list.sort()
    j1 = len(x1_list)

    # graph.sort()
    # print(graph)
    # incoming_e[a] = 0
    adjM = [[0 for _ in range(j1)] for _ in range(j1)]
    s4 = " "
    jess = []
    s5_list = []
    s6_list = []
    for i in range(x2):
        s5, s6 = input().split()
        # print(s6)
        s5 = int(s5)
        s5_list.append(s5)
        s6 = int(s6)
        s6_list.append(s6)
        adjM[s5][s6] = 1
        adjM[s6][s5] = 1

    s7 = input()
    s7 = int(s7)
    s8_nolist = []
    for i in range(s7):
        s8 = input()
        s8 = int(s8)
        s8_nolist.append(s8)
        #print(s8_nolist)
        for i in s8_nolist:
            for j in range(len(adjM)):
                for k in range(len(adjM)):
                    if j == i or k == i:
                        adjM[j][k] = 0
                        adjM[k][j] = 0
                # j = 0
            # for j in adjM[i]:
            #     adjM[i][j] = 0

        # for i in adjM:
        #     for j in adjM[i]:
        #         for k in s8_nolist:
        #             if adjM[i][j] == s8_nolist[k]:
        #                 adjM[i][j] == 0
        #  adjM[i][s8] = []

    lets_play_the_game = []
    have_we_seen = [False] * j1
    paths(0, (j1 - 1), have_we_seen, lets_play_the_game)
    # jess.sort()
    # print(jess)

    # if s5 not in jess:
    #   jess.append(s5)
    # if s6 not in jess:
    #   jess.append(s6)

    # j2 = len(jess)
    # print(j2)
    # print(s5_list)
    # print(s6_list)

    # for i in range(j2):
    #   if jess[i] == s5_list[i]:
    #      for j in range(j2):
    #         if jess[j] == s6_list[j]:
    #            adjM[i][j]=1

    # s7 = input()
    # s7 = int(s7)
    # for i in range(s7):
    #   s8 = input()
    #  s8 = int(s8)
    # if s8 in jess:
    #    jess.remove(s8)
    #   s5_list.remove(s8)
    #  s6_list.remove(s8)

    #print(f'{adjM}')
