#word = "пара-ра-рам рам-пам-папам па-ра-па-дам"
word = input("Введит естихотворение: ")
list1 = word.split()
print (list1)
counter = 0
count_list = []

for element in list1:
    for char in element:
        if char == "а":
            counter += 1
    count_list.append(counter)
    counter = 0

count_list = set(count_list)

if len(count_list) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
