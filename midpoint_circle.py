import matplotlib.pyplot as plt

def midpoint_circle(x_center, y_center, radius):
    x = 0
    y = radius
    d = 1 - radius


    plt.plot(x_center + x, y_center + y, 'ro')
    plt.plot(x_center + x, y_center - y, 'ro')
    plt.plot(x_center - x, y_center + y, 'ro')
    plt.plot(x_center - x, y_center - y, 'ro')
    plt.plot(x_center + y, y_center - x, 'ro')
    plt.plot(x_center - y, y_center + x, 'ro')
    plt.plot(x_center + y, y_center + x, 'ro')
    plt.plot(x_center - y, y_center - x, 'ro')

    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1


        plt.plot(x_center + x, y_center + y, 'ro')
        plt.plot(x_center + x, y_center - y, 'ro')
        plt.plot(x_center - x, y_center + y, 'ro')
        plt.plot(x_center - x, y_center - y, 'ro')
        plt.plot(x_center + y, y_center - x, 'ro')
        plt.plot(x_center - y, y_center + x, 'ro')
        plt.plot(x_center + y, y_center + x, 'ro')
        plt.plot(x_center - y, y_center - x, 'ro')

x_center = int(input("Enter x coordinate of center: "))
y_center = int(input("Enter y coordinate of center: "))
radius = int(input("Enter radius of circle: "))


midpoint_circle(x_center, y_center, radius)
plt.show()
