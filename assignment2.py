person = [{'name':'kassim','age':30,'hobby':['Movie','Traveling']},{'name':'Ufuk','age':29,'hobby':['Movie','Traveling']}]
print(person[0]['hobby'])
person_names = [el['name'] for el in person]
print(person_names)
all_person_older_than_20 = any([el['age'] > 20  for el in person ])
print(all_person_older_than_20)
person2 = person[:]
person2[0]['name']="Poul"
print(person2)