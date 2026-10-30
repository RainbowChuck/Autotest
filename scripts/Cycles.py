# -------------------Обратный отсчет-----------------------
def ca_boom(counter):
    if isinstance(counter, int):
        while counter >= 0:
            print(counter)
            counter -= 1
        print("Ca-Boom")
    else:
        print("Только Инты")
ca_boom(5)
ca_boom('2')

