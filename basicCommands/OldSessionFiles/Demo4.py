l1=[1,2,3]
try:
    print(1/0)
except ZeroDivisionError:
    print("zero division error observed")
except IndexError:
    print("index error observed")
except Exception:
    print("General error occured")
