import os, time
from processes6 import *

dict_shop = {
    # ชื่อสินค้า
    "name_product" : {
        1 : "notebook", 
        2 : "tablet",
        3 : "Mobile cs Phone"
    }, 
    # ราคาสินค้า
    "price_product" : {
        "notebook" : 34000, 
        "tablet" : 19000, 
        "Mobile cs Phone" : 26000
    }
}

product_List, price_List = [], []
amount_List1, price_discount_List = [], []

print("""🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 Welcome to csai shop 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
    1. notebook  =>     1           
    2. tablet    =>     2           
    3. Mobile    =>     3
    4. Exit      =>    -1""")
print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")

while True:
    try:
        product_input = int(input("Enter you product (1-3 and Exit : -1): "))
        if product_input == -1:
            break
        else:
            product_List.append(dict_shop["name_product"][product_input])
            product_List = list(set(product_List))
    except (ValueError, KeyboardInterrupt, KeyError):
        print("กรุณาป้อนเข้ามาทำงานใหม่อีกครั้ง")

os.system('cls'); time.sleep(1.5)

for amount in product_List:
    try:
        amount_input = int(input(f"Enter you amount_{amount}: "))
        amount_List1.append(amount_input)
    except ValueError:
        pass

for price in product_List:
    price_List.append(dict_shop["price_product"][price])

for price in range(len(price_List)):
    try:
        price1 = price_List[price] * amount_List1[price]
        price_discount_List.append(price1)
    except IndexError:
        price_discount_List.append("error".upper())
        price_discount_List = "".join(list(set(price_discount_List)))


if summation_process(amount2=price_discount_List) == "error":
    print("error".title())
else:
    summation_price = summation_process(amount2=price_discount_List)
    print("-"*49+f"\nราคารวมทั้งหมด : {summation_price:,.2f} บาท\n"+"-"*49)
        
    discount_price = discount_price_process(sum_price=summation_price)

    member_input = input("Yes : Y, No : N: ").upper()
    discount_member = discount_member_process(member=member_input)

    summation_discount = discount_price + discount_member
    price_discount = summation_price * (summation_discount / 100)
    sum_total = summation_price - price_discount
    print("-"*49+f"\nราคาสินค้าที่ลดแล้ว : {sum_total:,.2f} บาท\n"+"-"*49)
    try:
        money_input = int(input("Enter you money: "))
        os.system('cls'); time.sleep(1.5)
        input_receipt_process(money_input, sum_total, summation_price, price_discount, amount_List1 ,price_discount_List)
    except ValueError:
        print("กรุณาป้อนตัวเลขจำนวนเต็มเข้ามาทำงาน")