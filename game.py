import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_fallos = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
dificult =  int (input("""Ingrese un nivel de dificultad : 
                        1_ Fácil
                        2_ Media
                        3_ Difícil 
                       """))
word_displayed = ""
if dificult == 1:
    import esVocal
    for letter in secret_word:
        word_displayed += letter if esVocal.vocal(letter) else "_"
        if esVocal.vocal(letter):
            guessed_letters.append(letter)
elif dificult == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[len(secret_word)-1]
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[len(secret_word)-1])
else:
    word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


i = 0
while i < max_fallos:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter == "":
        print("Ingrese una letra valida")
        i += 1
        continue
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        i += 1
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
 # Verificar si la letra está en la palabra secreta
    if letter in secret_word: 
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        i += 1

# Mostrar la palabra parcialmente adivinada
letters = []
for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")
word_displayed = "".join(letters)
print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
if word_displayed == secret_word:
    print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
else:
    print(f"¡Oh no! Has alcanzado los {max_fallos} fallos permitidos.")
    print(f"La palabra secreta era: {secret_word}")