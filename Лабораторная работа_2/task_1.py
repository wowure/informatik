money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
salary_1 = salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money =money_capital + salary
month = 0
while money >= spend:
    month += 1
    salary -= spend
    money_capital += salary
    money = money_capital + salary_1
    salary = salary_1
    spend = spend+ spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", month)
