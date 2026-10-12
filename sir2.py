
# lists = """
# fever 10 Rs
# cold 10 Rs
# """
# medicin = {
#     "fever": 10,
#     "cold": 10
# }
# print(lists)
# enter_name = input("Enter medicine name: ").lower()
# quantity = int(input("Enter quantity: "))
# price = medicin[enter_name] * quantity
# print(f"Medicine: {enter_name}\nQuantity:{quantity}\nTotal:{price}")




# lists = """
# fever 10 Rs
# cold 10 Rs
# """
# medicin = {
#     "fever": 100,
#     "cold": 100
# }
# print(lists)
# enter_name = input("Enter medicine name: ").lower()
# quantity = int(input("Enter quantity: "))
# price = medicin[enter_name]*quantity
# if price>1000:
#   discount=price*0.10
#   price-=discount
#   print(f"Medicine: {enter_name}\nQuantity:{quantity}\ndiscount:{discount}\nTotal:{price}")
# else:
#   print(f"Medicine: {enter_name}\nQuantity:{quantity}\nTotal:{price}")


# lists = """
# fever 10 Rs
# cold 10 Rs
# """
# print(lists)
# medicin = {
#     "fever": 100,
#     "cold": 100
# }
# enter_name = input("Enter medicine name: ").lower()
# if enter_name not in medicin:
#   print("no medicin ")
# else:
#   quantity = int(input("Enter quantity: "))
#   if medicin[enter_name]>=quantity:
#     print(f"{quantity} is avaliable")
#   else:
#     print(f"sorry we have only {medicin[enter_name]} {enter_name} tablets ")





# lists = """
# fever 10 Rs
# cold 10 Rs
# """
# medicin = {
#     "fever": 10,
#     "cold": 10
# }
# print(lists)
# num = 0
# total = 0
# while num < 5:
#     enter_name = input("Enter medicine name: ").lower()
#     quantity = int(input("Enter quantity: "))
#     price = medicin[enter_name] * quantity
#     total += price
#     num += 1
# avg = total / num
# print(f"Total: {total} Rs\nAverage: {avg} Rs")

  


# month = int(input("Enter expiry month(1-12): "))
# year = int(input("Enter expiry year: "))
# from datetime import datetime
# current = datetime.now()
# if year < current.year or (year == current.year and month < current.month):
#     print("Medicine is expired")
# else:
#     print("Medicine is valid")


