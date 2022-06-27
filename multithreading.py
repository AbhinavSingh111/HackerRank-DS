import time
import threading
def calculate_square(numbers):
    print("Calculating Square of numbers : ")
    for i in numbers:
        time.sleep(0.2)
        print("Square : ",i*i)

def calculate_cube(numbers):
    print("Calculating Cube of numbers : ")
    for i in numbers:
        time.sleep(0.2)
        print("Cube : ",i*i*i)




if __name__=="__main__":
    numbers=[2,3,4,5,6]
    t=time.time()
    t1=threading.Thread(target=calculate_square,args=(numbers,))
    t2=threading.Thread(target=calculate_cube,args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Done in time : ", time.time()-t)
