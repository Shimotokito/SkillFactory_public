# вводим перемунную для количества билетов
tickets_num = int(input("Введите количество приобретаемых билетов: "))

# вводим пустой список куда будем записывать цену за каждый билет
prices_list = []

# цикл для рассчёт стоимости каждого билета
for ticket_number in range(tickets_num):
    age_for_ticket = int(input("Укажите возраст посетителя для билета №{}: ".format(ticket_number + 1)))
    if age_for_ticket >= 25:
        prices_list.append(1390)
    elif age_for_ticket >= 18:
        prices_list.append(990)
    else:
        prices_list.append(0)
# проверяем условие что количество билетов больше 3 и применяем скидку
if tickets_num > 3:
    print(f"Итоговая стоимость билетов со скидкой: {int(sum(prices_list) * 0.9)} рублей")
else:
    print(f"Итоговая стоимость: {sum(prices_list)} рублей")