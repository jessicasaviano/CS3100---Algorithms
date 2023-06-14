import math

if __name__ == "__main__":


    for i in range(2):
        x = int(input())
        dec = []
        inc = []
        equal = []
        for i in range(x):
            x1, x2 = input().split()
            x1 = int(x1)
            x2 = int(x2)
            if x1 > x2:
                dec.append([x1,x2])
            elif x2 > x1:
                inc.append([x1,x2])
            else:
                equal.append([x1,x2])




        dec = sorted(dec, key=lambda x: x[1])
        dec.reverse()
        inc = sorted(inc, key=lambda x: x[0])

        trailer = 0
        space = 0
        if len(inc) != 0:
            for i in range(len(inc)):
                if inc[i][0] > trailer+space:
                    trailer = trailer + (inc[i][0] - (space+trailer))
                space += inc[i][1] - inc[i][0]



        if len(equal) != 0:
            for j in range(len(equal)):
                if equal[j][0] > trailer + space:
                    trailer = trailer + (equal[j][0] - (trailer+space))
                space += equal[j][1] - equal[j][0]

        if len(dec) != 0:
            for k in range(len(dec)):
                if dec[k][0] > trailer + space:
                    trailer = trailer + (dec[k][0] - (space+trailer))
                space += dec[k][1] - dec[k][0]


        print(trailer)









