s = int(input('輸入分數:'))
if 0<=s and s<=100:
    if s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 70:
        print("C")
    elif s >= 60:
        print("D")
    elif s <= 59:
        print("E")