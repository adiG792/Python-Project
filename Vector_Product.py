
def vect_product():
    print("Vector Product\n")
    print("A = a1(i) + a2(j) + a3(k)\n")
    print("B = b1(i) + b2(j) + b3(k)\n")
    i1, j1, k1 = eval(input("a1 = ")), eval(input("a2 = ")), eval(input("a3 = "))
    i2, j2, k2 = eval(input("b1 = ")), eval(input("b2 = ")), eval(input("b3 = "))
    a = str(i1) + "i + " + str(j1) + "j + " + str(k1) + "k"
    b = str(i2) + "i + " + str(j2) + "j + " + str(k2) + "k"
    print("A =", a)
    print("B =", b, "\n")
    add = "+"
    if i1 == i2 and j1 == j2 and k1 == k2:
        print("Zero Vector")
    else:
        c1, c2, c3 = (j1 * k2) - (j2 * k1), (i2 * k1) - (i1 * k2), (i1 * j2) - (i2 * j1)
        if c1 != abs(c1) or c2 != abs(c2) or c3 != abs(c3):
            add = "-"
        c =  str(c1) + "i" + add + str(abs(c2)) + "j" + add + str(abs(c3)) + "k"
        print("A x B = \n")
        print(f"C = {c}")


vect_product()