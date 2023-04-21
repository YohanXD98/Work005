op = input("Digite sim ou não para continuar...")

while op != "não":
    dist = float(input("Digite a distância: "))
    temp = float(input("Digite o tempo: "))
    velo = dist/temp
    print("A velocidade média é:" ,velo)
    op = input("Digite sim ou não para continuar...")