import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
    xcoordinates = []
    ycoordinates = []

    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    p = 2 * dy - dx

    while x <= x1:
        if p >= 0:
            y = y + 1
            p = p + 2 * dy - 2 * dx
        else:
            p = p + 2 * dy

        x = x + 1


        print("x:", x, "y:", y)


        xcoordinates.append(x)
        ycoordinates.append(y)


    plt.plot(xcoordinates, ycoordinates, marker='o', markersize=3, markerfacecolor="red")
    plt.show()


print("Enter coordinates of first point: ")
x0 = int(input())
y0 = int(input())
print("Enter coordinates of second point: ")
x1 = int(input())
y1 = int(input())


bresenham(x0, y0, x1, y1)