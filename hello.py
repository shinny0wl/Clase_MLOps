import random
import hashlib


# Funcion para sumar dos numeros
def add(x, y):
    return x + y


# Funcion para generar un valor SHA-256 hash aleatorio (un valor hexadecimal)
def random_hash():
    random_value = str(random.random())
    return hashlib.sha256(random_value.encode()).hexdigest()


if __name__ == "__main__":
    print(add(1, 1))
    print(random_hash())
