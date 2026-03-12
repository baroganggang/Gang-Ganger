import random
def deck_shuffle():
  a=[]
  for i in range(2,11):
    for b in range(4):
      a.append(i)
  for i in range(12):
    a.append(10)
  for i in range(4):
    a.append("A")
  random.shuffle(a)
  return a

def calculate():
  dealer_v=count_value(dealer_deck)
  j=21-dealer_v
  if dealer_v<player_value:
    return True
  else:
    return False
def count_value(pdeck):
  clone_deck=pdeck.copy()
  As=clone_deck.count("A")
  value=0
  for b in range(As):
    clone_deck.remove("A")
  for i in clone_deck:
    value+=i
  if 21-value<10+As:
    value+=As
  else:
    value+=10+As
  return value
def pick_card(deck,sdeck):
  sdeck.append(deck[-1])
  deck.pop()
def player():
  pick_card(deck,player_deck)
  pick_card(deck,player_deck)
  print(player_deck)
  value=count_value(player_deck)
  v=input(": ")
  while v!="stay":
    if v=="pick":
      pick_card(deck,player_deck)
      print(player_deck)
      value=count_value(player_deck)
    if value>21:
      value=0
      break
    v=input(": ")
  return value
def dealer_bot():
  pick_card(deck,dealer_deck)
  pick_card(deck,dealer_deck)
  print(dealer_deck)
  better_take=calculate()
  va=count_value(dealer_deck)
  while better_take:
    pick_card(deck,dealer_deck)
    print(dealer_deck)
    va = count_value(dealer_deck)
    if va>21:
      va=0
      break
    better_take=calculate()
  return va

#Game_set
deck = deck_shuffle()
print(deck)
dealer_point=0
player_point=0
for i in range(3):
  #player
  player_deck=[]
  player_value=player()
  print(player_value)
  if player_value!=0:
    #dealer
    dealer_deck=[]
    dealer_value=dealer_bot()
    print(dealer_value)
    #point
    if player_value<dealer_value:
      dealer_point+=1
      print("Dealer point")
    elif player_value>dealer_value:
      player_point+=1
      print("Player point")
  else:
    dealer_point+=1
    print("Dealer point")
print()
print("Player: ",player_point)
print("Dealer: ",dealer_point)