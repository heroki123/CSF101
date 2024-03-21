num_multiply = int(input("enter the number you want to multilpy: "))
limit_num = int(input("enter the limit of number you want to multiply: "))
print(f"the multiplication of {num_multiply} till {limit_num} is: ")
for i in range(1,limit_num+1):
    print(f"{num_multiply} x {i} = {int(num_multiply*i)}")