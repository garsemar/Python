from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def print_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{} {}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_night = False
    while True:
        sleep(1)
        current_time += datetime.timedelta(hours=HOUR_DURATION)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True
        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                print_file_and_screen("Se ha hecho de noche.", "horas.txt")
            else:
                print_file_and_screen("Se ha hecho de dia.", "horas.txt")
        print_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")

# hours_file = open("horas.txt", "x")
# hours_file.write("Hola mundo")
# hours_file.close()

if __name__ == "__main__":
    main()
