def ricxvishedareba(x, y):
    if x>y:
        return (x, "მეტია", y, "-ზე", x/y, "ჯერ")
    if y>x:
        return (y, "მეტია", y, "-ზე", x/y, "ჯერ")

print(ricxvishedareba(10, 45))
