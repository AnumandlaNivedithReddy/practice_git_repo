# num=5
# for i in range(1,num+1):
#   print(" "*(num-i)+"*"*(2*i-1))


# def vc(word):
#   vowels=0
#   cons=0
#   word=word.lower()
#   for i in word:
#     if i in ['a','e','i','o','u']:
#       vowels+=1
#     elif i==" ":
#       continue
#     else:
#       cons+=1
#   return vowels,cons
# print( vc("this is a python class AE"))


# def count_vowels_consonants(s):
#     vowels = "aeiou"
#     vowel_count = 0
#     consonant_count = 0
#     for ch in s.lower():
#         if ch in vowels:
#             vowel_count += 1
#         elif ch.isalpha():
#             consonant_count += 1
#     return (vowel_count, consonant_count)
# print(count_vowels_consonants("Hello World"))



# def is_emirp(num):
#     org=num
#     if num<2:
#         return False
#     for i in range(2,num//2+1):
#         if num%i==0:
#             return False
#     num=str(num)
#     num=num[::-1]
#     num=int(num)
#     if num==org:
#         return False
#     for i in range(2,num//2+1):
#         if num%i==0:
#             return False
#     return True
# print("yes" if is_emirp(58) else "No")



# def is_palindrom(word):
#     word=word.lower()
#     return word==word[::-1]
# print("palindrom" if is_palindrom("madAm") else "not a palindrom")


# num=5
# for i in range(1,num+1):
#     print(" "*(num-i)+"*"*(2*i-1))


# num=1
# n=5
# for i in range(n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()


# num=5
# for i in range(num+1):
#     print("* "*i)
