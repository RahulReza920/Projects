items = []
sum=0

def addItem(price,name):
    items.append([name,price])

def displayMenu():
    global items
    print("Here's the menu for today:\n")
    print("ITEM_CODE\t\tITEM_NAME\t\tITEM_PRICE")
    print("-------------------------------------------------------------------")
    for n in range(0,len(items)):
        print(str(n+1)+".\t\t\t"+str(items[n][0])+"\t\tTk."+str(items[n][1]))
    print("-------------------------------------------------------------------")
def calculatePrice(code):

    global items
    global sum
    ordered_items=[]
    for item in code:
        ordered_items.append(int(item))

    
    for item in ordered_items:
        sum+=items[item-1][1]

    return sum

def displayOrder(code):
    global items
    print("BREAK DOWN OF YOUR ORDER:\n")
    print("ITEM_CODE\tITEM_NAME\tITEM_PRICE\tQUANTITY_ORDERED\tTOTAL_PRICE")
    ordered_items = []
    processed_items = ordered_items
    for item in code:
        ordered_items.append(int(item))
    for i in range(0,len(items)):

        quantity = 0
        price = 0
        for j in range(0,len(processed_items)):
            if(processed_items[j]==i+1):
                quantity+=1
                price+=items[i][1]



        if (quantity > 0):
            processed_items = [y for y in processed_items if y != i + 1]
            print(str(i + 1) + ".\t\t" + str(items[i][0]) + "\t\t" + str(items[i][1]) + "\t\t" + str(
                quantity) + "\t\tTk." + str(price))


addItem(10,"Samosa  ")
addItem(15,"SinGara  ")
addItem(35,"Bun Samosa")
addItem(30,"Oreo Milkshake")
addItem(15,"Chicken Chop")
addItem(50,"Pizzaa      ")
addItem(40,"Burger      ")
addItem(30,"Sandwich    ")
addItem(100,"Biriyani   ")

while(True):
    print("Welcome to our store.\n")
    displayMenu()
    order=input("What would you like to order today? ")
    displayOrder(order)
    print()
    print("Your  final bill amount is Tk."+str(calculatePrice(order)))
    print()
    choice=input("Do you want to order again? (Y/N)")
    if(choice=="N" or choice=="n"):
        print()
        print("==========================")
        print("Thank you for shopping with us.")
        break
    print()
    print("==========================")