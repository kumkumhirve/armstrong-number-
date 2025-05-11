def armstrong(number):
    length = len(str(number))
    temp = number
    sum = 0

    while temp>0:
        digit = temp%10
        sum += digit ** length
        temp = temp // 10
    print(number,sum)
    if sum == number:
        print("the number is armstrong")
    
    else:   
        print("the number is not armstrong")

armstrong(1634)


