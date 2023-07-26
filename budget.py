import math

class Category:
  def __init__(self, nam):
    self.name = nam
    self.balance = 0
    self.ledger = []
    
  def deposit(self, amount, description = ""):
    self.balance += amount
    self.ledger.append({
      'amount': amount,
      'description': description    
    })
    
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({
      'amount': -amount,
      'description': description
    })
      return True
    return False

    #sufficient funds to take place
    

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
      return True
    return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    return True

  def __str__(self):
    asterisks = "*" * ((30 - len(self.name)) // 2)
    deposit_string = asterisks + self.name + asterisks + "\n"
    
    for i in range(len(self.ledger)):
      
      if len(self.ledger[i]['description']) > 23:
        deposit_string += (
          self.ledger[i]['description'][:23] + " "
        )
      else:
        deposit_string += (
          self.ledger[i]['description'] + " "*(30 - len(self.ledger[i]['description']) - len(str("{:.2f}".format(self.ledger[i]['amount']))))
        )
      deposit_string += str("{:.2f}".format(self.ledger[i]['amount'])) + "\n"

    deposit_string += "Total: " + str(self.balance)
    return deposit_string
    
def create_spend_chart(categories):
  if len(categories) > 4:
    return "Too many categories given"

  total_withdrawals = 0

  #calculate total withdrawals
  for cat in categories:
    for ta in cat.ledger:
      if ta['amount'] < 0:
        total_withdrawals += (ta['amount']*-1)

  total_withdrawals = round(total_withdrawals, 2)

  print(total_withdrawals)
  
  cat_percent = dict()

  for cat in categories:
    spent_money = 0
    for ta in cat.ledger:
      if ta['amount'] < 0:
        spent_money += (ta['amount']*-1)

    cat_percent[cat.name] = (int(spent_money * 100 / total_withdrawals) // 10) * 10

    
  chart_string = "Percentage spent by category\n"

  chart_string += make_percent_string(100, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(90, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(80, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(70, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(60, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(50, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(40, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(30, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(20, categories, cat_percent) + "\n"
  chart_string += " " + make_percent_string(10, categories, cat_percent) + "\n"
  chart_string += " "*2 + make_percent_string(0, categories, cat_percent) + "\n"
  
  chart_string += " "*4 + "-"*(len(make_percent_string(0, categories, cat_percent)) - 2) + "\n"


  max_name_length = max([len(category.name) for category in categories])

  for i in range(max_name_length):
        chart_string += "     "
        for category in categories:
            if i < len(category.name):
                chart_string += f"{category.name[i]}  "
            else:
                chart_string += "   "

        if i != max_name_length - 1:
          chart_string += "\n"

  return chart_string

def make_percent_string(percent, categories, cat_percent):
  chart_string = str(percent) + "|"

  for cat in categories:
    if cat_percent[cat.name] >= percent:
      chart_string += " o "
    else: 
      chart_string += " "*3

  chart_string += " "

  return chart_string
  