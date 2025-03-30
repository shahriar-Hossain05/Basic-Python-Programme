og_price = float(input("Enter the original price of the product(a positive number): "))

if og_price > 0 :
    discount = float(input("Enter a discount percentage (a number between 0 and 100): "))
    
    if 0 <= discount <= 100 :
        damount = og_price * discount / 100
        final_price = og_price - damount

        print(f" Discount amount = ${damount:.2f}")
        print(f"Final price: ${final_price:.2f}")

    else :
       print("Error: Discount percentage must be between 0 and 100!")

else :
   print("Error: The original price must be a positive number!")    