def tips_calculator(bill, guests, persentage):
    """Calculate the tip per guest.

    :param bill: float - the cost of service without tips.
    :param quests: int - the number of quests who will split the tips.
    :param persentage: int - desired tip as a persentage of the bill.
    :return: float - tips per quest in nmonetary value .

    This function takes 3 paramenters representing the cost of service, number of quests and desired tip persenatge 
    and returns the tip amount per quest.
    """

    tip = float(bill) * persentage / 100
    return tip / guests

print(tips_calculator(120,3,15))