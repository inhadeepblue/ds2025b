def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result.append(city)
    return result

cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
# cities = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(set(duplicate_city(cities)))