# cost=int(input("enter the cost price:"))
# selling=int(input("enter the selling price:"))
# if selling>cost:
#   print("seller is in proffit")
# elif selling==cost:
#   print("no proffit no loss")
# else:
#   print("seller is in loss")



# principal_amount=int(input("enter principle amount:"))
# annual_interest_rate=int(input("enter anual interst:"))
# time_years=int(input("enter time in years:"))
# interst=(principal_amount*annual_interest_rate*time_years)/100
# total=principal_amount+interst
# print(f"amount={principal_amount}\nrate={annual_interest_rate}\ntime={time_years}")
# print(f"interst={interst}\ntotal={total}")




# principal_amount = float(input("Enter principal amount: "))
# annual_interest_rate = float(input("Enter annual interest rate (%): "))
# time_years = int(input("Enter time in years: "))
# amount = principal_amount * (1 + annual_interest_rate / 100) ** time_years
# interest = amount - principal_amount
# print(f"Total Amount: {amount:.2f}")
# print(f"Compound Interest : {interest:.2f}")




# price=int(input("enter the price:"))
# discount=float(input("enter the discount:"))
# discount_price=discount/100
# total=price-(price*discount_price)
# print(f"total={price}\ndiscount={discount_price}\nafter discount={total}")




# price=int(input("enter the price:"))
# gst=int(input("enter the gst percentage:"))
# gst_price=price*gst/100
# total=price+gst_price
# print(f"price={price}\ngst={gst_price}\ntotal={total}")


# with open(r"C:\Users\anuma\Desktop\source.xls", "rb") as file1:
#     data = file1.read()
# with open(r"C:\Users\anuma\Desktop\destination.xls", "wb") as file2:
#     file2.write(data)
# print("Data copied successfully!")




# import shutil
# source = r"C:\Users\anuma\Downloads\pandas\4_read_write_to_excel\read_write_with_flask\example2.xlsx"
# destination = r"C:\Users\anuma\Downloads\pandas\4_read_write_to_excel\stocks_weather.xlsx"
# shutil.copyfile(source, destination)
# print("File copied successfully!")







import pandas as pd
src = pd.read_excel(r"C:\Users\anuma\Downloads\source.xlsx")
dest = pd.read_excel(r"C:\Users\anuma\Downloads\destination.xlsx")
dest[src.columns[::2]] = src.iloc[:, ::2]
dest.to_excel(r"C:\Users\anuma\Downloads\destination.xlsx", index=False)
print("Copied successfully!")




import pandas as pd
src = pd.read_excel(r"C:\Users\anuma\Downloads\source (1).xlsx")
dest = src[src["Salary"] > 40000]
dest.to_excel(r"C:\Users\anuma\Downloads\destination (1).xlsx", index=False)
print("Data copied successfully!")

