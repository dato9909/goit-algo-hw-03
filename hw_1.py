from datetime import datetime


def get_days_from_today(date):
    try:
        a = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = current_date - a
        return delta.days
    
    except ValueError:
        print('Неправильнный ввод данных')

print(get_days_from_today('2024-02-01'))
    
        
