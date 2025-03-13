def policz(a,b,c):
    return (a+b)*c-10

def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError as zde:
        print(f"dzielenie przez 0 -> {zde}")
    else:
        print(wynik)
