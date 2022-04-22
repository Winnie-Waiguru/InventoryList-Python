print('''
---------------------------------      
      Welcome to Angelic close
---------------------------------
      1.View Items
      2.Buy Items
      3. Exit 
''')

userOption= int(input("Pick option 1, 2 or 3: "))
print("Show items")
items =open("list.txt", "r")
item_data= items.readlines()
print("--------------------------")
for i in item_data:
    print(i)
    print("--------------------------")
print(item_data)