price_rub = int(input("Введите цену пирожка в рублях: "))
price_kop = int(input("Введите цену пирожка в копейках: "))
quantity = int(input("Введите количество пирожков: "))
total_price = price_rub * 100 + price_kop
total_sum_kop = total_price * quantity
total_rub = total_sum_kop // 100
total_kop = total_sum_kop % 100
print(f"Сумма к оплате: {total_rub} руб. {total_kop} коп.")