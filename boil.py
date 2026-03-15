room_temp = 20  # комнатная температура

def boil(water_temp):
    while water_temp < 100:
        water_temp = water_temp + 10
        print('Текущая температура:', water_temp, 'C')
    else:
        print('Чайник закипел!')

boil(room_temp)