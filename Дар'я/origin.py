import time

def read_file(name):
    try:
        file = open(name, "r")
        print(file.read())
    except Exception as e:
        print(e)
    finally:
        file.close()
        print("Programa zavershena")

read_file("text.txt")

time.sleep(50)