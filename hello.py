import random
import hashlib


# Funcion para sumar dos numeros
def add(x, y):
    return x + y


def random_hash():
    # Genera un valor aleatorio SHA-256 hash (un valor hexadecimal)
    random_value = str(random.random())
    return hashlib.sha256(random_value.encode()).hexdigest()


if __name__ == "__main__":
    print(add(1, 1))
    print(random_hash())
