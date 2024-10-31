import time
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            file.write(word + '\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# Вызов функции в основном потоке
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")


# Создание и запуск дополнительных потоков
start_time = time.time()

threads = []
for word_count, file_name in [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]:
    thread = Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Общее время выполнения: {end_time - start_time:.2f} секунд")