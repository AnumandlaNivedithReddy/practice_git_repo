# def sum_prime():
#     count = 0
#     num = []
#     i = 2
#     while count < 25:
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             num.append(i)
#             count += 1
#         i += 1
#     print(sum(num))
# sum_prime()



# print("anagram" if sorted("listen")==sorted("silent") else "not")



# nums = [100,4,200,1,3,2,2,5]
# nums.sort()
# count = 1
# longest = 1
# for i in range(1, len(nums)):
#     if nums[i] == nums[i-1]:
#         continue
#     elif nums[i] == nums[i-1] + 1:
#         count +=1
#     else:
#         count=1
#     longest=max(longest, count)
# print(longest)



# num=[100,1,5,3,2,4,800]
# num.sort()
# count=1
# largest=1
# for i in range(1,len(num)):
#     if num[i]==num[i-1]:
#         continue
#     elif num[i]==num[i-1]+1:
#         count+=1
#     else:
#         count=1
#     largest=max(count,largest)
# print(largest)

# def is_anagram(word1,word2):
#     if sorted(word1)!=sorted(word2):
#         return False
#     return True
# word1="listen"  
# word2="silent"
# print("yes" if is_anagram(word1,word2) else "no")


# num=[10,20,1,2,3,5,6,4,11,12,13,14,15,16,17,18]
# num.sort()
# count=1
# longest=1
# for i in range(1,len(num)):
#     if num[i]==num[i-1]:
#         continue
#     elif num[i]==num[i-1]+1:
#         count+=1
#     else:
#         count=1
#     longest=max(count,longest)
# print(longest)


# list=[1,2,3,4,6,7,8,9,10]
# for i in range(1,11):
#   if i not in list:
#     print(i)
 

# def sec_largest(num):
#   num=str(num)
#   largest=0
#   second=0
#   for i in num:
#     if int(i)>largest:
#       second=largest
#       largest=int(i)
#     elif int(i)<largest and int(i)>second:
#       second=i
#   return second
# print(sec_largest(583535))   
    


# def even_rev(num):
#   num=str(num)
#   even_digits=list(filter(lambda x: int(x)%2==0,num ))
#   result=""
#   for i in num:
#     if int(i)%2==0:
#       result+=even_digits.pop(-1)
#     else:
#       result+=i
#   return result
# print(even_rev(12345678))

