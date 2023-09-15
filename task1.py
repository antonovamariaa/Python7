#word = "пара-ра-рам рам-пам-папам па-ра-па-дам"
# не знаю, как сделать через lambda
def Input(str):
    word = input(str)
    list1 = word.split()
    return list1

def Poem(list1):
    counter = 0
    count_list = []
    for element in list1:
        for char in element:
            if char in "аоуиыэеёюя":
                counter += 1
        count_list.append(counter)
        counter = 0

    if len(set(count_list)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")


Poem(Input("Введит естихотворение: "))
