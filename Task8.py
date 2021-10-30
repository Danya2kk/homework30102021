inviteList = []

for i in range(3):
    inviteList.append(input("Введите имя человека которого хотите пригласить: "))

while True:
    option = input("Хотите кого-то пригласить еще yes/no: ")
    if option == "yes":
        newName = input("Введите имя приглашенного: ")
        inviteList.append(newName)
    elif option == "no":
        break

for name in inviteList:
    print(name)