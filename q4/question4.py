def facto(n):
    if n == 0:
        return 1
    return n*facto(n-1)

def main():
    for i in range(15)[0:15:2]:
        print("{}! = {}".format(i, facto(i)))

if __name__ == '__main__':
    main()

