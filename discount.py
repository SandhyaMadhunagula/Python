"""1.if the mobile brand is Apple then the discount is 10% else the discount is 5%
   2.all shoes have 2% tax and no discount"""
#-------------------------->
def purchase_product(product_type, price, mobile_brand = None):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        total_price = price + price * 2 / 100

    print("Total price of " +product_type+ " is "+str(total_price))

purchase_product("Mobile", 20000, "Apple")
purchase_product("Shoe", 300)
                                                
