import db_tools as dt
from ATM import ATM


def get_atm_list():
    atm_list = dt.select_info_from_db('id', 'atm', all=True)
    return [x[0] for x in atm_list]

print('Банкомати:')
atm_list = get_atm_list()
for atm in atm_list:
    print(f'№{atm}')

atm_num = input('Виберіть номер банкомата, в якому бажаєте провести операцію: ')
if atm_num not in atm_list:
    print('Банкомата з таким номером не існує. Завершую роботу')
else:
    atm = ATM(int(atm_num))
    atm.start()
