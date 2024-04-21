import random
import math

# Problem alanı sınırları / Problem area boundaries
lower_bound = -10
upper_bound = 10
# Popülasyon boyutu / Population size
population_size = 10
# İterasyon sayısı / Number of iteration
max_iterations = 100
# Karga arama algoritması parametreleri / Parameters of CSA
pa = 0.25  # Pa: Karga aşağı düşme oranı / Crow down fall rate
fl = 2  # Fl: Karga uçuş uzunluğu faktörü / Crow flight length factor
alpha = 0.5  # Alpha: Karga yer değiştirme oranı / Crow displacement rate

# Fitness fonksiyonu / Fitness function
def fitness(x):
    return x**2

# Başlangıç popülasyonunu oluştur / Create starter population
population = [random.uniform(lower_bound, upper_bound) for _ in range(population_size)]

for _ in range(max_iterations):
    # Her karga için / For every crow
    for i in range(population_size):
        # Karganın bulunduğu konumu al / Take the crow's position
        current_position = population[i]
        # Karganın uçuş uzunluğunu hesapla / Calculate the crow's flight length
        step_size = fl * random.uniform(-1, 1)
        # Yeni konumu hesapla / Calculate the new position
        new_position = current_position + step_size
        # Yeni konumu sınırlara taşı / Move the new location to the borders
        new_position = max(min(new_position, upper_bound), lower_bound)
        # Fitness değerlerini karşılaştır / Compare fitness values
        if fitness(new_position) < fitness(current_position):
            # Yeni konumu kabul et / Accept new location
            population[i] = new_position
        else:
            # Yeni konumu kabul etme, karga aşağı düşsün / Do not accept the new position, let the crow fall down
            if random.random() < pa:
                population[i] = new_position
    # En iyi çözümü bul / Find the best solution
    best_solution = min(population, key=fitness)
    print("Iteration:", _, "Best Solution:", best_solution, "Fitness:", fitness(best_solution))
