import threading
import time

def worker(num):
    print(f"Thread {num}: Strating")
    time.sleep(2)
    print(f"Thread {num}: Finishing")

t=[]
for i in range(3):
    tt=threading.Thread(target=worker,args=(i,))
    t.append(tt)
    tt.start()

for tt in t:
    tt.join()

print("All threads completed.")