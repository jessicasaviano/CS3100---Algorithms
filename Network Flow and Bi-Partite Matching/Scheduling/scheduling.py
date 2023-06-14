
def dfs(j, match, seen):
    global v
    for v in range(length_of_courses):

        if adjM[j][v] and seen[v] == False:
            seen[v] = True

            if match[v] != -1 or match[v] == -1 or dfs(match[v], match, seen) == True:

                match[v] += j

                return True

    return False



if __name__ == "__main__":
    global v
    x1 = float('inf')
    x2 = float('inf')
    x3 = float('inf')
    while x1 != 0 and x2 != 0 and x3 != 0:
        x1, x2, x3 = input().split()

        x1 = int(x1)
        x2 = int(x2)
        x3 = int(x3)
        if x1 == 0 and x2 == 0 and x3 == 0:
            break

        people = {}
        people_list = []
        people_count = -1
        index_count = 0
        course_count = []
        x = 0
        storing = []
        for i in range(x1):
            y1,y2 = input().split()
            if y1 not in people_list:
                people_list.append(y1)
            if y2 not in storing:
                storing.append(y2)

            if y1 not in people.keys():
                people[y1] = [y2]


            if y1 in people.keys():
                if y2 not in people[y1]:
                    people[y1] += [y2]

        adjM = [[0 for _ in range(len(storing))] for _ in range(len(people_list))]

        #print(people)

        #print(people_list)

        #print(storing)
        for j in range(len(people_list)):
            temp_person = people_list[j]
            for k in range(len(people[temp_person])):
                adjM[j][storing.index(people[temp_person][k])] = 1

        #print(adjM)


        list_of_max_cap = []
        for i in range(x2):
            a,b = input().split()
            b = int(b)
            list_of_max_cap.append([a,b])


        #print(list_of_max_cap)

        results = []

        for i in range(len(people_list)):
            results.append([people_list[i], 0])
        length_of_people = len(people_list)
        length_of_courses= len(storing)
        #print(length_of_people)
        #print(length_of_courses)
        match = [-1] * (length_of_courses)
        for j in range(x3):
            for i in range(length_of_people):
                seen = [False] * (length_of_courses)
                #print(seen)
                #print(dfs(i, match, seen))
                if dfs(i, match, seen):
                    if results[i][1] < list_of_max_cap[v][1]:
                            results[i][1] += 1


        #print(results)

        #print(num)
        lens = 0
        for i in range(len(results)):
            lens += results[i][1]


        #print(lens)
        list_to_test = [True] * length_of_people

        for i in range(len(results)):
            if results[i][1] == x3:
                list_to_test[i] = False

        #print(list_to_test)
        if lens == length_of_people * x3 and not any(list_to_test):
            print('Yes')

        else:
            print('No')

        x1 = 0
        x2 = 0
        x3 = 0


























#
# def dfs(j, match, seen):
#     global num
#     num = ''
#
#     for v in range(length_of_courses):
#         num = storing[v]
#         if adjM[j][v] and adjM[j][v] >0 and seen[v] == False:
#             seen[v] = True
#
#             if match[v] == -1 or dfs(match[v], match, seen):
#                 match[v] = j
#                 adjM[j][v] -= 1
#
#                 return True
#
#
#     return False
#
#
#
# if __name__ == "__main__":
#     global num
#     x1 = float('inf')
#     x2 = float('inf')
#     x3 = float('inf')
#     while x1 != 0 and x2 != 0 and x3 != 0:
#         x1, x2, x3 = input().split()
#         if x1 == 0:
#             print('Yes')
#         if x3 == 0:
#             print('Yes')
#         x1 = int(x1)
#         x2 = int(x2)
#         x3 = int(x3)
#         if x1 == 0 and x2 == 0 and x3 == 0:
#             break
#
#         people = {}
#         people_list = []
#         people_count = -1
#         index_count = 0
#         course_count = []
#         x = 0
#         storing = []
#         for i in range(x1):
#             y1,y2 = input().split()
#             if y1 not in people_list:
#                 people_list.append(y1)
#             if y2 not in storing:
#                 storing.append(y2)
#
#             if y1 not in people.keys():
#                 people[y1] = [y2]
#
#
#             if y1 in people.keys():
#                 if y2 not in people[y1]:
#                     people[y1] += [y2]
#
#         adjM = [[0 for _ in range(len(storing))] for _ in range(len(people_list))]
#
#         #print(people)
#
#         #print(people_list)
#
#
#         list_of_max_cap = []
#         for i in range(x2):
#             a,b = input().split()
#             b = int(b)
#             list_of_max_cap.append([a,b])
#
#
#         #print(list_of_max_cap)
#         #print(storing)
#         for j in range(len(people_list)):
#             temp_person = people_list[j]
#             for k in range(len(people[temp_person])):
#                 adjM[j][storing.index(people[temp_person][k])] = list_of_max_cap[storing.index(people[temp_person][k])][1]
#
#         results = []
#         people[people_list[i]].remove(storing[i])
#         print(storing)
#         tem_people = {}
#         temp_people = people
#
#         for i in range(len(people_list)):
#             results.append([people_list[i], 0])
#
#         length_of_people = len(people_list)
#         length_of_courses= len(storing)
#
#         match = [-1]*length_of_courses
#         for j in range(x3):
#
#             for i in range(length_of_people):
#                 temp_people = people
#                 print(temp_people)
#                 seen = [False] * length_of_courses
#                 while dfs(i, match, seen):
#                     print("yo")
#                     print(results)
#                     if len(temp_people[people_list[i]]) > 0 and num in temp_people[people_list[i]]:
#                         results[i][1] += 1
#                         print(num)
#                         print(people[people_list[i]])
#                         temp_people[people_list[i]].remove(num)
#
#
#         print(results)
#
#
#
#         print(adjM)
#         #print(results)
#         #print(num)
#         lens = 0
#         for i in range(len(results)):
#             lens += results[i][1]
#
#
#         #print(lens)
#         list_to_test = [True] * length_of_people
#
#         for i in range(len(results)):
#             if results[i][1] == x3:
#                 list_to_test[i] = False
#
#         print(list_to_test)
#         if lens == length_of_people * x3 and not any(list_to_test):
#             print('Yes')
#
#         else:
#             print('No')
#
#         x1 = 0
#         x2 = 0
#         x3 = 0