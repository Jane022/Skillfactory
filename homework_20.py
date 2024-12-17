import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

#1
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2
max_quantity = 0
max_order = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'Номер заказа с самым большим количеством товаров: {max_order}, количество товара: {max_quantity}')

#3
new_dict = {}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    new_dict[date] = new_dict.get(date, 0) + 1
max_orders = max(new_dict.values())
for date in sorted(new_dict):
    if new_dict[date] == max_orders:
        print(f'{date} было сделано больше всего заказов, количество заказов {max_orders}')
#4
user_id_dict = {}
orders_max = 0
max_user = ''

for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_id_dict[user_id] = user_id_dict.get(user_id, 0) + 1
for user_id, count in user_id_dict.items():
    if count > orders_max:
        orders_max = count
        max_user = user_id
print(f'Пользователь {max_user} сделал большее число заказов: {orders_max}')

#5
max_user = ''
sum_orders_dict = {}
max_price = 0

for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    price = orders_data['price']
    sum_orders_dict[user_id] = sum_orders_dict.get(user_id, 0) + price

for user_id, price in sum_orders_dict.items():
    if price > max_price:
        max_price = price
        max_user =  user_id
print(f"У пользователя {max_user} самая большая сумма заказов: {max_price}")

#6
total_sum = 0
for order_num, orders_data in orders.items():
    total_sum +=  orders_data['price']

orders_count = len(orders)
average_price = total_sum / orders_count
print(f"Средняя стоимость заказа в июле: {average_price} ")

#7
total_price = 0
total_quantity = 0

for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    total_price += price
    total_quantity += quantity
product_average_price = total_price / total_quantity
print(f'Средняя стоимость товаров в июле: {product_average_price}')