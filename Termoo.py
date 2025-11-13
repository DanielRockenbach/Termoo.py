import random

# Listas de palavras

palavras_5 = [ "Ameno", "Anime", "Audio", "Aureo", "Eiras", "Meias", "Menos", "Mundo", "Reais", "Reino", "Rosna", "Radio", "Seria", "Somar", "Serio"]

palavras_6 = ["Amorfo", "Brinco", "Cresce", "Duvida", "Escuta", "Fardos", "Gostar", "Horror", "Imagem", "Jogada", "Lembre", "Molhar", "Nuvens", "Oculto", "Puxado"]

palavras_7 = ["Abraçar", "Brinque", "Cuidado", "Desafio", "Esperar", "Fechado", "Gritava", "Habitam", "Imagine", "Jornada", "Lembrar", "Navegar", "Ocultar", "Pousada", "Quartzo"]



# Metodo que avalia posicao de cada letra em relacao a palavra sorteada
def avalia_chute(chute, palavra):
    result = ""
    palavra = palavra.lower()
    chute = chute.lower()
    for i in range(len(palavra)):
        if chute[i] == palavra[i]:
            result += "\033[32m" + chute[i] # As letras ficam verdes quando corretas
        elif chute[i] in palavra:
                result += "\033[33m" + chute[i] # As letras ficam amarelas quando corretas, porem na posição errada
        else:
            result += "\033[0m" + chute[i] # As letras ficam brancas quando incorretas
    return result + "\033[0m"

# Metodo responsavel pelo funcionamento do jogo, sorteando uma das palavras das listas, de acordo com a dificuldade e comparando-a com o palpite do jogador
def termo(dificuldade):
    segredo = random.choice(dificuldade).lower()
    tamanho = len(segredo)
    tentativas = 1
    MAX_TENTATIVAS = len(segredo)

    while tentativas <= MAX_TENTATIVAS:
        chute = input("Digite seu palpite: ").lower()
        if len(chute) !=  tamanho:
            print(f"Tentativa invalida, digite uma palavra em portugues com {tamanho} letras.")
            continue
        if chute == segredo:
            print("Parabéns! Você acertou qual era a palavra secreta: ",segredo.upper())
            print ("Seu numero de tentativas utilizadas: ", tentativas)
            break

        tentativas += 1
        feedback = avalia_chute(chute, segredo)
        print(feedback)

    if tentativas > MAX_TENTATIVAS:
        print("GAME OVER! Suas tentativas acabaram. A palavra secreta era: ", segredo)

# Metodo de exibicao do menu principal
def menu():
    print("Bem vindo, vamos jogar! ")
    print("Escolha seu modo de jogo: ")
    print("Digite 5 para: Palavras com 5 letras (5 tentativas) ")
    print("Digite 6 para: Palavras com 6 letras (6 tentativas) ")
    print("Digite 7 para: Palavras com 7 letras (7 tentativas) ")
    print("")

# Metodo de ativacao do jogo
def main():
    while True:
        menu()
        modo = input("Selecione o modo de jogo (5, 6 ou 7): ").strip()
        if modo == "5":
            dificuldade = palavras_5
            return termo(dificuldade)
        elif modo == "6":
            dificuldade = palavras_6
            return termo(dificuldade)
        elif modo == "7":
            dificuldade = palavras_7
            return termo(dificuldade)
        else:
            print('VALOR INVALIDO. Digite 5,6 ou 7.')
            print("")
            continue


if __name__ == "__main__":
    main() 