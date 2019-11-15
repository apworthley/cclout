def fib():
    fibs = [1, 2]
    n=0
    for i in range(1,9):
        fibs.append(fibs[n]+fibs[n+1])
        n+=1
        

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
