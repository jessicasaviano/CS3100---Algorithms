import math

if __name__ == "__main__":
    overall = []
    x1 = int(input())
    for i in range(x1):
        b, m, c = input().split()
        b = int(b)
        keep = b
        m = int(m)
        c = int(c)
        ans = []
        cost = 0

        for j in range(c):
            name, one, two = input().split()
            one = int(one)
            two = int(two)
            b = keep
            j += 1
            cost = 0
            if b - m == 1:
                cost = cost + one
                ans.append([name, cost])

            while b > m+1:
                if b - m == 1:
                    cost = cost + one
                    break
                if math.ceil((b/2.0)) > m:
                    cost = cost + two
                    b = float(b)
                    b = math.ceil((b / 2.0))

                else:
                    b = b - 1
                    cost = cost + one

            if [name,cost] not in ans:
                ans.append([name, cost])

        ans = sorted(ans, key=lambda x: x[1])

        print("Case" + " " + str(i + 1))
        for k in range(len(ans)):
            print(str(ans[k][0])+" "+str(ans[k][1]))



