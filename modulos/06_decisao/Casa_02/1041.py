x, y = input().split()
x, y = float(x), float(y)

if (x == 0) and (y == 0):
    print("Origem")
else:
    if (x == 0): # y != 0
        print("Eixo Y")
    else:
        if (y == 0): # x != 0
            print("Eixo X")
        else:        
            if (x > 0):
                if (y > 0):
                    print("Q1")
                else:
                    print("Q4")
            else:
                if (y > 0):
                    print("Q2")
                else:
                    print("Q3")