def gas_tanks(tank1, tank2, tank3):
    gas_average = (tank1 + tank2 + tank3) / 3

    return f"""
    Total gas average: {gas_average}%
    Tank 1: {tank1}%
    Tank 2: {tank2}%
    Tank 3: {tank3}%
"""
print(gas_tanks(10,15,20))