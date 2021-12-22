inter = [int(inter) for inter in input().split(" ")]
hidd = [int(hidd) for hidd in input().split(" ")]
inter.pop(0)
hidd.pop(0)
si = 0
while True:
    if max(inter) >= max(hidd):
        si = 1
        if not inter and hidd:
            inter.remove(max(inter))
            hidd.remove(max(hidd))
        else:
            break
    else:
        print("Espera")
        break
if int(si) == 1:
    print("Corre!")
