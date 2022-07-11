if __name__ == '__main__':
    def print_func(n):
        if 1 <= n <= 150 :
            for i in range(1,n+1) :
                print(i, end ='') # To replace default new line (end = '\n') with same line (end = '')
    n = int(input())
    print_func(n)