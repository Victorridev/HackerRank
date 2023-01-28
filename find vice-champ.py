if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) 
    unique_arr_numbers = list(set(arr))
    vice_sem_repeticao = sorted(unique_arr_numbers)
    vice_real = vice_sem_repeticao[-2]
    
    print(vice_real)
    
    
    
   
        