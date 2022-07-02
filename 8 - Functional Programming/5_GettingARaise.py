"""
You work on a payroll program.
Given a list of salaries, you need to take the bonus everybody is getting as 
input and increase all the salaries by that amount.
Output the resulting list.

Current attempt, have tried several iterations:
"""
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
def add_bonus(salaries):
    return salaries + bonus

result = list(map(add_bonus, salaries))

print(result)