guest = ''
while guest != 'q':
    guest = input('Введите имя гостя (q for exit): ')
    with open('guest.txt', 'a') as file_object:
        file_object.write(f"{guest}\n")
    print(f"Thank you, {guest.title()}! You are booked")
