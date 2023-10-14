cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

profit_loss = selling_price - cost_price

if profit_loss > 0:
    print("You made a profit of", profit_loss)
elif profit_loss < 0:
    print("You incurred a loss of", -profit_loss)
else:
    print("You broke even; there's neither profit nor loss.")
