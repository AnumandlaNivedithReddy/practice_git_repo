'''1. Even / Odd'''

# def even_or_odd (num):
#   if num%2==0:
#     return True
#   else:
#     return False
# if even_or_odd(127):
#   print("even number")
# else:
#   print("odd number")



'''2. Prime'''

# def is_prime(num):
#   for i in range(2,num//2+1):
#     if num%i==0:
#       return False
#     else:
#       return True
# if is_prime(170):
#   print("prime")
# else:
#   print("not a prime")
    
'''3. Palindrome'''

# def is_Palindrome(par):
#   par=str(par)
#   return par==par[::-1]
# if is_Palindrome(121):
#   print("palindrom")
# else:
#   print("not a palindrom") 

'''4. Factorial'''

# from functools import reduce
# def Factorial(num):
#   result=reduce(lambda x,y:x*y,range(1,num+1))
#   return result
# print(Factorial(5))




# def factorial(num):
#   total=1
#   for i in range(1,num+1):
#     total*=i
#   return total
# print(factorial(5))

'''5. Strong '''


# def is_strong(num):
#   total=0
#   count=1
#   for i in str(num):
#     for j in range(1,int(i)+1):
#       count*=j
#     total+=count
#     count=1
#   return total==num
# if is_strong(145):
#   print("strong number")
# else:
#   print("not a strong")


# def is_strong(num):
#   org=num
#   fac=0
#   total=1
#   while num>0:
#     digit=num%10
#     for i in range(1,digit+1):
#       total*=i
#     fac+=total
#     total=1
#     num//=10
#   return org==fac
# print("strong " if is_strong(40585) else "not strong")

from functools import reduce
# def is_strong(num):
#   total=0
#   for i in str(num):
#     total+=reduce(lambda x,y:x*y,range(1,int(i)+1),1)
#   return total==num
# print("strong" if is_strong(2) else "not strong")

'''6. Armstrong'''

# def is_armstrong(num):
#   total=0
#   for i in str(num):
#     total+=int(i)**len(str(num))
#   return total==num
# print("armstrong" if is_armstrong(371) else "not armstrong")



# def is_armstrong(num):
#   org=num
#   total=0
#   while num>0:
#     digit=num%10
#     total+=digit**len(str(org))
#     num//=10
#   return org==total
# print("armstrong" if is_armstrong(135) else "not armstrong")


# def is_armstrong(num):
#   total=0
#   num_str=str(num)
#   result=reduce(lambda x,y: x+int(y)**len(num_str),num_str,0)
#   total+=result
#   return total==num
# print("armstrong" if is_armstrong(153) else "not armstrong")


'''7. Disarium'''

# def is_disaram(num):
#   org=num
#   total=0
#   pos=len(str(num))
#   while num>0:
#     last_digit=num%10
#     total+=last_digit**pos
#     pos-=1
#     num//=10
#   return org==total
# print("disaram" if is_disaram(89) else "not disaram")
    
    
'''8. Happy'''

# def is_happy(num):
#   while num!=1:
#     total=0
#     while num!=0:
#       last_digit=num%10
#       total+=last_digit**2
#       num//=10 
#     num=total
#   return total==1
# print("happy" if is_happy(27) else "not happy")

  