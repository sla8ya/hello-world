import csv
FILENAME = "SPISOCHEK.csv"
print("Привет, давай попробуем заполнить список, для выходна нажми N")
while True:
    dlina = input("Введи количество данных списка: ")
    if dlina != int():
        print("Необходимо ввести число! ")
    else:
        if dlina.lower() == "n":
            print("До свидания")
        else:
            dlina = ()
            i = 0
            spisok = list()
            znak = ()
            while i < int(dlina):
                znak = str((input("Вводи значение для добавление в список: ")))
                spisok.append(str(znak))
                print(spisok)
                i = i + 1
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file, delimiter="\t")
                for row in spisok:
                    writer.writerow(row)
    print("Работа программы успешно завершена")
