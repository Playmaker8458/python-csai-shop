def summation_process(amount2):
    if amount2 == 'ERROR':
        return "error"
    else:
        return sum(amount2)

def discount_price_process(sum_price : int) -> int:
    if sum_price > 50000:
        return 10
    else:
        return 0

def discount_member_process(member : str) -> int:
    if member == "Y":
        return 5
    else:
        return 0

def input_receipt_process(money : int, sumtotal : int, summation_price : int, price_discount : int, amount1 : list, money_pay : list):
    if money < sumtotal:
        print("กรุณากรอกจำนวนเงินเข้ามาทำงานใหม่อีกครั้ง")
    else:
        price_notebook = money_pay[0] if len(money_pay) > 0 else 0
        price_tablet = money_pay[1] if len(money_pay) > 1 else 0
        price_phone = money_pay[2] if len(money_pay) > 2 else 0

        amount_notebook = amount1[0] if len(amount1) > 0 else 0
        amount_tablet = amount1[1] if len(amount1) > 1 else 0
        amount_phone = amount1[2] if len(amount1) > 2 else 0

        amount_total = amount_notebook + amount_tablet + amount_phone

        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 ใบเสร็จ 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
        print(f"รายการทั้งหมด {amount_total} รายการ")
        if amount_notebook > 0:
            print(f"1.Notebook {amount_notebook} เครื่อง ราคา {price_notebook:,.2f} บาท")
        if amount_tablet > 0:
            print(f"2.Tablet {amount_tablet} เครื่อง ราคา {price_tablet:,.2f} บาท")
        if amount_phone > 0:
            print(f"3.Mobile cs Phone {amount_phone} เครื่อง ราคา {price_phone:,.2f} บาท")
        print(f"\nราคารวมก่อนหักส่วนลด: {summation_price:,.2f} บาท")
        print(f"ยอดส่วนลด: {price_discount:,.2f} บาท")
        print(f"ราคารวมหลังหักส่วนลด {sumtotal:,.2f} บาท")
        print(f"จำนวนเงินทอน: {money - sumtotal:,.2f} บาท")
        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")