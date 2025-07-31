# Multiprocessing allows a Python program to run multiple processes in parallel — each with its own memory space and Python interpreter.
# It helps to fully utilize multiple CPU cores, overcoming the Global Interpreter Lock (GIL) limitation in CPython.

# Always use if __name__ == "__main__": to avoid recursive process spawning (especially on Windows).

import time
from multiprocessing import Process
from PIL import Image
import os


# 1
def calc_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    print(f"Factorial of {n} is calculated.")


if __name__ == "__main__":
    numbers = [50000, 60000, 70000]

    processes = [Process(target=calc_factorial, args=(num,))
                 for num in numbers]

    start = time.time()
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = time.time()

    print("Time taken:", end - start)


# 2
def resize_image(path):
    img = Image.open(path)
    img = img.resize((300, 300))
    img.save(f"resized_{os.path.basename(path)}")
    print(f"{path} resized.")


if __name__ == "__main__":
    images = ["img1.jpg", "img2.jpg", "img3.jpg"]
    processes = [Process(target=resize_image, args=(img,)) for img in images]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
