dataArr = []

def get_data(var_name, text):
    data = input(text)
    while data == "":
        data = input("tkaia zaniari daxl bka : ")
    dataArr.append([var_name, data])


def save_to_file(person):
    file = open("adress_book.txt", "a")
    for data in person:
        file.write(f"{data} = {person[data]} \n")
    file.write("________________________ : \n")

def create_person(dataArr):
    person = {}
    for x in dataArr:
        person[x[0]] = x[1]
    save_to_file(person)




get_data("name", "nawek daxl bka : ")
get_data("age", "taman daxl bka : ")
get_data("adress", "nawnishan daxl bka : ")
get_data("tel", "talafun daxl bka : ")
get_data("work", "Kar daxl bka : ")

create_person(dataArr)