inimigos = [(50, 30), (100, 100), (10, 90), (30, 25)]

for x, y in inimigos:
    print(f"A posição é X={x} e Y={y}")

x = int(input("Informe a posição X que deseja arriscar! "))    
y = int(input("Informe a posição Y que deseja arriscar! "))    

if (x, y) in inimigos:
    inimigos.remove((x, y))
    print("Você acertou um inimigo!")
else:
    print("Água! Você errou!")    

print(inimigos)
