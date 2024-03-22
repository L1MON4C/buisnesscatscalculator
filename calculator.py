a = int(input("Цена самого дешевого, через которого деньги: "))
b = int(input("Цена дорогого мальчика: "))
c = int(input("Цена дорогой девочки: "))

# creditZoo = 40 - (b + c) - a
# moneyZoo = 40 + creditZoo
# moneyBuyCatsZoo = moneyZoo - 7
# creditPit = (moneyBuyCatsZoo - (b + c)) - 21
# print(creditPit)
# creditForEach =
money_Pit = 40 - 21
money_Zoo = 40 - a - 7
print(f"Доступные у питомника {money_Pit}, Доступные у зоо {money_Zoo},\ всего {money_Zoo + money_Pit}")
total_Money = money_Pit + money_Zoo
total_Credit = total_Money - (b + c)
credit_For_Each = float((total_Credit / 2) * (-1))
print(f"Общее кол-во недостающих монет(кредит) - {total_Credit}")
print(f"Кредит для каждого - {credit_For_Each}(за сколько покупает дешевого котенка питомник 1 сезон)")
