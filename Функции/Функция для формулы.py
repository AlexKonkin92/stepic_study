def f(x):
    if x <= -2:
        x = 1 - ((x + 2)**2)
    elif -2 < x <= 2:
        x = - (x / 2)
    elif x > 2:
        x = ((x - 2)**2) + 1
    return (x)