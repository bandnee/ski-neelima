Write a small utility using a countDownLatch for executing the threads all at one time .

import threading

class countDownLatch:

    def countDown():

    def await(self):
        while count != 0 :
            wait;
    def done:
    


def worker(cd,rd,dl):

    #Wait for the countDown Latch to become 0
    #union of the threads
    cd.countDown()
    cd.await()
    rd.countDown()
    #Do the real work
    dl.done()
    return

threads = []
cd = countDownLatch()
rd = countDownLatch()

for i in range(5)
    t = threading.Thread(target=worker, cd, rd)
    threads.append(t)
    t.start()

rd.await()
t0 = get_time()
for i in range(5):
    t.join()




