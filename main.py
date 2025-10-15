import logging

logging.basicConfig(
    filename='cube.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cube(n):
    """
    Возвращает куб числа.
    """
    result = n * n * n
    logging.info(f"Вызов функции cube({n}) дает результат: {result}")
    return result

if __name__ == "__main__":
    print(cube(2))
    print(cube(-3))
    print(cube(4))
