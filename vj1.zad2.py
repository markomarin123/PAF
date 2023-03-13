x1=float(input("unesi tocku x1 "))
y1=float(input("unesi tocku y1 "))
x2=float(input("unesi tocku x2 "))
y2=float(input("unesi tocku y2 "))

k=(y2-y1)/(x2-x1)
l=y1-k*x1
print("y={}x+{}".format(k,l))