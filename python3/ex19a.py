def order_stats(total_orders, total_returns):
    print(f"You have {total_orders} orders")
    print(f"You have {total_returns} returns")
    print(f"Your net sales are {total_orders - total_returns}")
    print("Hopefully you had a good month!\n")

#1.Simple arguments
order_stats(4321, 1111)

#2.Math
order_stats(102+431, 200*4)

#3.Variables
x_sales = 231
y_sales = 777
z_sales = 64
returns = 23
order_stats(x_sales+y_sales+z_sales, returns)

#4.Variables and Math
order_stats((x_sales*3)+(y_sales%3)+(z_sales/2), returns)

#5.With a vaariable number of arguments
var_stats = (530, 42)
order_stats(*var_stats)

#6.function to function?
def func_to_func():
    value1 = 20
    value2 = 30
    order_stats(value1, value2)
func_to_func()

#7.Calling inside a variable
net = order_stats(30,20)

#8. Assign the function to a Variable
net_try = order_stats
net_try(30,1)

#9.user input - Don't forget to specify a type of input! In this case an integer
print("how much did you sell this month?")
user_sales = int(input('>>>'))
order_stats(user_sales, returns)
