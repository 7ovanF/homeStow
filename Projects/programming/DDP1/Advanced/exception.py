def whos_older(x,y):
    if !isinstance(x, "tuple") or !isinstance(y, "tuple"):
        raise TypeError("Invalid type")
    if len(x) != 2 or len(y) != 2:
        raise ValueError("Invalid tuple length")
    x_nama, x_umur = x[0], x[1]
    y_nama, y_umur = y[0], y[1]
    if !isinstance(x_nama, "str") or !isinstance(x_umur, "int") or !isinstance(y_nama, "str") or !isinstance (y_umur, "int"):
        raise ValueError("Invalid tuple content type")

    if x_umur > y_umur:
        return x_nama
    elif x_umur < y_umur:
        return y_nama
    else:
        return None

print(whos_older(("buds", 50), "adi"))
