# making a fancy but simple menu for the restaurant  is complete here
menu={"Pizza": 299,
    "Burger": 149,
    "Sandwich": 99,
    "Pasta": 199,
    "Momos": 129,
    "Biryani": 249,
    "Fried Rice": 189,
    "Chicken Roll": 89,
    "Paneer Tikka": 179,
    "Cold Coffee": 79}

#Greeting our customer and showing the menu..
print("Welcome to our PY_EATS Restaurant")
print("Pizza: 299\nBurger: 149\nSandwich: 99\nPasta: 199\nMomos: Rs129\nBiryani: Rs249\nFried Rice: Rs189\nChicken Roll: Rs89\nPaneer Tikka: Rs179\nCold Coffee: Rs79")

#grab the customer order and make the total amount of the bill it will stored in the "Total_amount_Order" variable( like 99+79=178Rs will be stored in "Total_amount_Order")
Total_amount_Order=0

order_1=input("Enter the name of the Food you would like to enjoy!= ")  # taking the customer order
if (order_1 in menu):                                                   # cheaking the item is available in our restraunt or not
    Total_amount_Order += menu[order_1]                                 # it will increse the amount(like before ordering the )
    print(f"Your item {order_1}  has been added to your order") 

else:
    print(f"Sir please order something else that we can serve you\n ordered item {order_1} is not avaialable yet.")  #if the customer order a item is not in a list

another_order= input("Do you want to add another item? (Yes/No)=  ")                             #checking the customer order another item or not
if (another_order=="Yes"): 
    order_2= input("Enter the second item you want to order = ")                                #if the  customer wants another order 
    if (order_2 in menu):
      Total_amount_Order += menu[order_2]                                                        #updating the new total amount of the order
      print(f"Your item{order_2} has been added tour order")

    else:(f"Sir please order something else that we can serve you\n ordered item {order_2} is not avaialable !")      # if the customer order something as a second item which is not in the list..

print(f"The total amount of your bill is = {Total_amount_Order}")                                             # the value you have to pay for the food

print(" 🌟 Thank you for visiting us 🌟")
