from collections import defaultdict

#worked with nathan barnette jnb8kry

if __name__ == "__main__":
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    #print(x1)
    #print(x2)

    graph = {}
    incoming_e = {}
    for i in range(x1):
        a = input()
        graph[a] = []
        incoming_e[a] = 0

    s4 = " "
    for i in range(x2):
        s4 = input()
        s4 = s4.split()

        graph[s4[1]] += [s4[0]]

        incoming_e[s4[1]] += 1


    #print(graph)
    #print(incoming_e)

    zero_node = []
    arr = []
    for key in incoming_e:
        if incoming_e[key] == 0:
            zero_node.append(key)
            # print("hi")
    while zero_node:
        zero_node.sort()
        x = zero_node.pop(0)
        # print("hi")
        # print(zero_node)
        for key in graph:
            if x in graph[key]:
                incoming_e[key] -= 1
            if incoming_e[key] == 0 and key not in zero_node and key not in arr and not (key == x):
                zero_node.append(key)
        arr.append(x)
    print(*arr)






