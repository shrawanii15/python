
states = []
area = []
population = []


for i in range(5):
    print(f"\nEnter details for State {i+1}")
    
    name = input("State Name: ")
    a = float(input("Area: "))
    p = int(input("Population: "))
    
    states.append(name)
    area.append(a)
    population.append(p)


print("\n----- State Information -----")
for i in range(5):
    print(states[i], "- Area:", area[i], ", Population:", population[i])


max_area = max(area)
index_area = area.index(max_area)
print("\nState with Largest Area:", states[index_area])


max_pop = max(population)
index_pop = population.index(max_pop)
print("State with Largest Population:", states[index_pop])


density = []
for i in range(5):
    d = population[i] / area[i]
    density.append(d)

print("\nPopulation Density of States:")
for i in range(5):
    print(states[i], ":", density[i])


max_density = max(density)
index_density = density.index(max_density)
print("\nState with Highest Population Density:", states[index_density])