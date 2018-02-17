'''d = {
    "name1": {"city": None, "temperature": None, "wind": None},
    "a": {"city": "Moscow", "temperature": 11, "wind": 60},
    "b": {"city": "London", "temperature": 13, "wind": 110},
    "c": {"city": "New-York", "temperature": 17, "wind": 77}
}
name = input("Input your name: ")
#if name in d.keys():
print(
	 d.get(name,{}).get("city"),
	 d.get(name,{}).get("temperature"),
	 d.get(name,{}).get("wind")
	 ,)
#else:
#	print("Nothing found for " + name)
'''

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}

names = ['Оля', 'Петя', 'Вася', 'Маша']
#print('\n'.join(names))
for name in names:
	print(name, len(name), "Male" if is_male[name] else "Woman")

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print("Total: " + str(len(groups)))
for group in groups:
	ppl = ', '.join(group)
	print("Subgroup has: " + str(len(group)) + ". Members are: " + ppl + ".")

#d = {a: {"city": b, "f2": c, "f3": d} for a,b,c,d in zip(range(3),range(1,4),list("Hello"), list("Medved"))}
from collections import ChainMap as cm
d = {1: 1, 2: 2}
c = {1: 11, 3: 3}
cd = cm(c,d)
for a in (c,d,cd):
	print(a, dict(a))