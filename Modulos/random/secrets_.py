# secrets gera números aleatórios seguros

import secrets
import string as s
from secrets import SystemRandom as Sr

random = secrets.SystemRandom()  # realmente é aleatório

# print(secrets.randbelow(100))
# print(secrets.choice([1, 10, 11, 99, 25]))

# random.seed(10)  # está sendo ignorado

# r_range = random.randrange(10, 20, 2)
# print(r_range)


# r_int = random.randint(10, 20)
# print(r_int)


# r_uniform = random.uniform(10, 20)
# print(r_uniform)


# nomes = ["Luiz", "Maria", "Helena", "Joana"]
# random.shuffle(nomes)
# print(nomes)


# novos_nomes = random.sample(nomes, k=2)
# print(nomes)
# print(novos_nomes)


# novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# print(random.choice(nomes))


# Criando uma senha:

print()
print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
print()
