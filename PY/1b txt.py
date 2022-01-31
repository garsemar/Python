from multiprocessing import Process, cpu_count
import time
from os import system


def counter(num):
    count = 0
    nom = 1
    while count < num:
        count += 1
        system(f'cd /home/sjo/Escriptori && echo '
               f'"holaawdaowkdapowdapwjdawkjdlkawjdlkawlkdjawlkdjawlkdjlakwjdalwkdjalkwjd" > hola{nom}.txt')
        nom += 1


def main():
    print(cpu_count())

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()
