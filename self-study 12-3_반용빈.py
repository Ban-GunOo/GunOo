import threading

def sum(low, high):
    total = 0
    for i in range(low,high+1):
        total += i;
    print("1+2+3+...+",high,"=",total)

add1 = threading.Thread(target = sum,args =(1,1000))
add2 = threading.Thread(target = sum,args =(1,100000))
add3 = threading.Thread(target = sum,args =(1,10000000))

add1.start()
add2.start()
add3.start()