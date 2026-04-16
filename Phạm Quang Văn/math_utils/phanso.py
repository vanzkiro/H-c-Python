def cong_ps(a, b, c, d):
        return (a * d + b * c, b * d)

def tru_ps(a, b, c, d,):
    return(a * d - b * c, b * d)

def nhan_ps(a, b, c, d):
    return(a * c, b * d)

def chia_ps(a, b, c, d):
    if c == 0:
        raise ZeroDivisionError("Khong the chia cho phan so co tu = 0")
    return(a * d + b * c)