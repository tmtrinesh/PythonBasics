import random
deck = list(range(1,53))
random.shuffle(deck)
greetings = ["Chennai","Bangalore","Delhi","Hyderabad"]

colors = ['Red','Black','Blue']


hand = random.sample(deck,k=5)
results = random.choices(colors,weights = [18,18,2],k=10)

number = random.uniform(1,10)
value = random.randint(0,7)
string = random.choice(greetings)



print(string +'_ Corey!_')
print(number)
print(value)

print(results)
print(deck)
print(hand)