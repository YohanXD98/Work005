id = int(input("Digite a idade: "))
count01 = 0
count02 = 0

while id >= 0:
    if id <=15:
        count01 = count01 +1
    else:
        count02 = count02 +1
    id = int(input("Digite a idade: "))

print(count01)
print(count02)