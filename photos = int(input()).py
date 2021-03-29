photos = int(input())
price = 0

if int(photos) <= 5:
  price = photos * 7
elif int(photos) >= 6 and int(photos) <= 10:
  price = 35 + (int(photos) - 5) * 6.8
elif int(photos) >= 11 and int(photos) <=20:
  price = 69 + (int(photos) - 10) * 6.5
else:
  price = 134 + (int(photos) - 20) * 6.2
  
print(f"The total price will be {price}")
print(f"The price for each piece will be {price / photos}")

x = 0

for x in range(int(photos)):
  print(price)