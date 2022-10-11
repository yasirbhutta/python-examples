# https://yasirbhutta.github.io/python/
# https://web.facebook.com/groups/pythontips

thisdict = {
  "rollno": 5,
  "name": "Muhammad Ahmad",
  "university": "Ghazi University DG Khan",
  "age":25  
}
print(thisdict["name"]) ##Output: Muhammad Ahmad

# for loop with dict
names = {'hamza': 'lion', 'yasir': 'well to do'}
for n, m in names.items():
  print(f'name: {n}, meaning: {m}')