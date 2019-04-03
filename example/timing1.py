"""
File: timing1.py
Prints the running tiimes for problem sizes that double,
using a single loop
"""
import time

problemSize = 100
iterations = 0


def work1(problemSize):
    work = 1
    for _ in range(problemSize):
        global iterations
        iterations += 1       
        work += 1
        work -= 1


def work2(problemSize):
    work = 1
    for _ in range(problemSize):
        for _ in range(problemSize):
            global iterations
            iterations += 1       
            work += 1
            work -= 1


if __name__ == '__main__':

    # print('%12s%16s' % ('Problem Size', 'Seconds'))
    print('{:_>12}{:>16}{:>12}'.format('Problem Size', 'Seconds', 'iterations'))

    for count in range(5):

        start = time.time()
        # The start of the algorithm
        work2(problemSize)
        # The end of the algorithm
        elapsed = time.time() - start

        # print('%12d%16.3f' % (problemSize, elapsed))
        print('{:>12d}{:16.3f}{:>12d}'.format(problemSize, elapsed, iterations))
        problemSize *= 2
