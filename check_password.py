def check_password(password):
    if password == '0000':
        print('Пароль устарел. Попробуй другой!')
    if password == '123':
        print('Доступ разрешен. Сигнализация отключена!')
    else:
        print('Сработала сигнализация. Вызываю ГБР!')
        
check_password('0000')