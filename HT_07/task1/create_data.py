import os
import random

with open('data/users.data') as users_file:
    users = users_file.read().split('\n')
    users = [user.split(', ')[0] for user in users]
    for user in users:
        dir_path = f'data/{user}_data'
        try:
            os.mkdir(dir_path)
        except OSError:
            pass

        # Створення та заповнення файлів
        with open(f'{dir_path}/{user}_balance.data', 'w') as user_balance:
            user_balance.write(str(random.randint(1000, 100000)))
        with open(f'{dir_path}/{user}_transactions.data', 'w') as user_transactions:
            pass
