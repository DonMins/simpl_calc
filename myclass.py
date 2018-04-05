def f(a1,a2,a3,a4,a5,x):
    if x==1:
        return a1
    if x==2:
        return a2
    if x==3:
        return a3
    if x==4:
        return a4
    if x==5:
        return a5

def norm(ved,sb):
    ved2=[]
    for i in range(len(ved)):
        ved2.append(ved[i]/ved[sb])
    return ved2

def func(a1,a2,a3,a4,a5,dj,st,sb):
    sb = sb - 1
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    res5 = []
    dj2 = []


    ved0 = f(a1,a2,a3,a4,a5,st)
    ved = norm(ved0,sb)

    for j in range(len(a1)):
        res1.append(a1[j] - ved[j] * a1[sb])
        res2.append(a2[j] - ved[j] * a2[sb])
        res3.append(a3[j] - ved[j] * a3[sb])
        res4.append(a4[j] - ved[j] * a4[sb])
        res5.append(a5[j] - ved[j] * a5[sb])
        dj2.append(dj[j] - ved[j] * dj[sb])
    if st==1:
        print("a1=",ved)
        print("a2=",res2)
        print("a3=",res3)
        print("a4=",res4)
        print("a5=",res5)
        print("dj=",dj2)
    if st==2:
        print("a1=", res1)
        print("a2=", ved)
        print("a3=", res3)
        print("a4=", res4)
        print("a5=", res5)
        print("dj=", dj2)
    if st == 3:
        print("a1=", res1)
        print("a2=", res2)
        print("a3=", ved)
        print("a4=", res4)
        print("a5=", res5)
        print("dj=", dj2)
    if st == 4:
        print("a1=", res1)
        print("a2=", res2)
        print("a3=", res3)
        print("a4=", ved)
        print("a5=", res5)
        print("dj=", dj2)
    if st == 5:
        print("a1=", res1)
        print("a2=", res2)
        print("a3=", res3)
        print("a4=", res4)
        print("a5=", ved)
        print("dj=", dj2)

if __name__ == "__main__":

    a1 = [40, -4, 3, 1, 0, 0, 0, 0]
    a2 = [6, 0, 1, 0, 1, 0, 0, 0]
    a3 = [-4, 1, -4, 0, 0, 1, 0, 0]
    a4 = [-1, -1, -1, 0, 0, 0, 1, 0]
    a5 = [20, 6, -3, 0, 0, 0, 0, 1]
    dj = [0, -1, -6, 0, 0, 0, 0, 0]

    a1 = [37.0, -3.25, 0.0, 1.0, 0.0, 0.75, 0.0, 0.0]
    a2 = [5.0, 0.25, 0.0, 0.0, 1.0, 0.25, 0.0, 0.0]
    a3 = [1.0, -0.25, 1.0, -0.0, -0.0, -0.25, -0.0, -0.0]
    a4 = [0.0, -1.25, 0.0, 0.0, 0.0, -0.25, 1.0, 0.0]
    a5 = [23.0, 5.25, 0.0, 0.0, 0.0, -0.75, 0.0, 1.0]
    dj = [6.0, -2.5, 0.0, 0.0, 0.0, -1.5, 0.0, 0.0]

    func(a1,a2,a3,a4,a5,dj,3,3)
