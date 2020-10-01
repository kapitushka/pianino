import winsound

melody = [1,1,1,2,1,1,2,3,1,4,4,4,5,3,6,2,3,1]
for c in melody:
    if c== 0:
        time.sleep(0.5)
    if c == 1:
        winsound.Beep(261, 500)
    if c == 2:
        winsound.Beep(293, 500)
    if c == 3:
        winsound.Beep(329, 500)
    if c == 4:
        winsound.Beep(349, 500)
    if c == 5:
        winsound.Beep(392, 500)
    if c == 6:
        winsound.Beep(440, 500)
    if c == 7:
        winsound.Beep(493, 500)
    if c == 8:
        winsound.Beep(523, 500)

while True:
    player_select = input("Введите последовательность цифр от 1 до 8: ")
    speed_select  = int(input("Введите скорость проигрывания от 1 до 10: "))
    print("Ваша мелодия нотами:")

    for c in player_select:
        if c == "1":
            winsound.Beep(261, speed_select * 100)
            print("До")
        if c == "2":
            winsound.Beep(293, speed_select * 100)
            print("Ре")
        if c == "3":
            winsound.Beep(329, speed_select * 100)
            print("Ми")
        if c == "4":
            winsound.Beep(349, speed_select * 100)
            print("Фа")
        if c == "5":
            winsound.Beep(392, speed_select * 100)
            print("Соль")
        if c == "6":
            winsound.Beep(440, speed_select * 100)
            print("Ля")
        if c == "7":
            winsound.Beep(493, speed_select * 100)
            print("Си")
        if c == "8":
            winsound.Beep(523, speed_select * 100)
            print("До")
