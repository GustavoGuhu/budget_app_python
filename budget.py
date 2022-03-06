class Category:
    
  def __init__(self, cat):
    self.cat = cat
    self.ledger = []
    self.funds = 0
    self.total_withdraw = 0
  
  def __str__(self):
    ns = 30 - len(self.cat)
    nsh = int(ns/2)
    op = nsh * "*" + self.cat + nsh * "*" + "\n"
    lines =[]
    total = 0
    for k in self.ledger:
      desc = str(k.get("description"))
      amount = k.get("amount")
      lin = ""
      if len(desc) > 23:
        desc = desc[0:23]
      else:
        num = 23-len(desc)
        desc += num * " "
      lin += desc
      total += amount 
      amount = "{:.2f}".format(amount)
      if len(amount) > 7:
        amount = amount[0:7]
      else:
        num = 7-len(amount)
        amount = num * " " + amount
      lin += amount + "\n"
      lines.append(lin)
    lin_total = "Total: {:.2f}".format(total)
    lines.append(lin_total)
    for i in lines:
      op += i
    return op
  
  def deposit(self, amount, description=""):
    self.amount = amount
    self.funds += amount
    self.description = description
    line = {"amount":self.amount, "description":self.description}
    self.ledger.append(line)

  def withdraw(self, amount, description=""):
    self.amount = -amount  
    self.description = description
    self.total_withdraw += self.amount
    if self.check_funds(amount):
      self.funds += self.amount
      line ={"amount":self.amount, "description":self.description}
      self.ledger.append(line)
      return True
    else:
      return False
   
  def get_balance(self):
    return self.funds
  
  def transfer(self, amount, o_cat):
    self.amount = -amount
    if self.funds + self.amount >= 0:
      self.funds += self.amount
      desc = "Transfer to %s" % (o_cat.cat)
      line ={"amount":self.amount, "description":desc}
      self.ledger.append(line)
      o_cat.funds += amount
      desc = "Transfer from %s" % (self.cat)
      line = {"amount":-self.amount, "description":desc}
      o_cat.ledger.append(line)
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.funds - amount >= 0:
      return True
    else:
      return False

def create_spend_chart(categories):
  lines = ["Percentage spent by category", "100| ", " 90| ", " 80| ", " 70| ", " 60| ", " 50| ", " 40| ", " 30| ", " 20| ", " 10| ", "  0| " ]
  total = 0
  percentages = []
  for i in categories:
    total += i.total_withdraw
  
  cp = 0
  for i in categories:
    pc = (i.total_withdraw/total) *10
    pc = int(pc)
    percentages.append(pc)

  for i in percentages:
    num = 11 - i
    for l in range(num, 12):
      lines[l] = lines[l] + "o  "
    for l in range (1, num):
      lines[l] = lines[l] + "   "
    

  lines.append("    " + len(categories) * "---" + "-")
  
  mn = 0
  for i in categories:
    if len(i.cat) > mn:
      mn = len(i.cat)
  
  lins = []
  for i in range (0, mn):
    lins.append("     ")
  
  for i in categories:
   for k in range(0, len(i.cat)):
    lins[k] += i.cat[k]  + "  "
   for k in range(len(i.cat), mn):
    lins[k] += "   "


 
  lines = lines + lins

  graph = ""
  for i in lines:
#    i = i.rstrip()
    graph += i +"\n" 
  
  graph = graph[:len(graph)-1]

  #print(repr(graph))
  return graph
