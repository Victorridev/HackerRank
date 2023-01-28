if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    X = [i for i in (x+1)]
    Y = [i for i in (y+1)]
    Z = [i for i in (z+1)]
 
    print([[a,b,c] for a in X for b in Y for c in Z if a+b+c != n ])