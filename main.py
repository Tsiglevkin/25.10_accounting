from application import salary as s
from application.db import people as p
from datetime import datetime


if __name__ == '__main__':
    print(f'Текущая дата и время - {datetime.now()}.')
    print()
    s.calculate_salary(s.salary_dict)
    p.get_employees()
