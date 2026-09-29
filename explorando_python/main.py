import random
 
cardapio = {
    "chocolate": 12.00,
    "morango": 10.00,
    "flocos": 11.00,
    "ninho": 13.00,
    "limao": 9.00
}
 
brindes = ["Casquinha extra grátis", "Cobertura de chocolate", "Desconto de 15% na próxima"]
 
def mostrar_cardapio():
    print("\n--- CARDÁPIO DA SORVETERIA ---")
    for sabor, preco in cardapio.items():
        print(f"{sabor.title()}: R$ {preco:.2f}")
 
def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor = input("\nEscolha um sabor (ou 'fechar' pra pagar): ").lower()
        if sabor == "fechar":
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor.title()} adicionado!")
        else:
            print("Esse sabor não existe no cardápio")
    return pedido, total
 
mostrar_cardapio()
pedido, total = fazer_pedido()
 
print(f"\nSeu pedido: {pedido}")
print(f"Total: R$ {total:.2f}")
 
if total > 20:
    print(f"Parabéns, você ganhou: {random.choice(brindes)}")