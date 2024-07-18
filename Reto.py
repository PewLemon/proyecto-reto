import random


class Player:
    def __init__(self, name, language):
        self.name = name
        self.position = 0
        self.coins = 5
        self.language = language

    def move(self):
        steps = random.randint(1, 6)  # roll a dice to determine steps
        self.position += steps
        if self.language == 'English':
            print(f"{self.name} rolled the dice and got {steps}")
            print(f"{self.name} moved {steps} steps and is now at position {self.position}")
        elif self.language == 'Spanish':
            print(f"{self.name} lanzó el dado y obtuvo {steps}")
            print(f"{self.name} se movió {steps} pasos y ahora está en la posición {self.position}")

    def challenge(self, other_player):
        if self.coins >= 1:
            self.coins -= 1
            if self.language == 'English':
                print(f"{self.name} challenges {other_player.name} with a card!")
            elif self.language == 'Spanish':
                print(f"{self.name} desafía a {other_player.name} con una carta!")

            result = random.choice([True, False])  # Simulating the result of the challenge
            lost_steps = random.randint(1, 4)  # Random steps to be moved back

            if result:
                self.coins += 2  # Winning the challenge gives 2 coins
                if self.language == 'English':
                    print(f"{self.name} won the challenge and gained 2 coins!")
                    print(f"{other_player.name} moves back {lost_steps} steps.")
                elif self.language == 'Spanish':
                    print(f"{self.name} ganó el desafío y obtuvo 2 monedas!")
                    print(f"{other_player.name} retrocede {lost_steps} pasos.")
                other_player.position -= lost_steps  # Losing player moves backward
            else:
                other_player.coins += 1  # Losing the challenge makes the other player gain 1 coin
                if self.language == 'English':
                    print(f"{self.name} lost the challenge. {other_player.name} gained 1 coin!")
                    print(f"{self.name} moves back {lost_steps} steps.")
                elif self.language == 'Spanish':
                    print(f"{self.name} perdió el desafío. ¡{other_player.name} obtuvo 1 moneda!")
                    print(f"{self.name} retrocede {lost_steps} pasos.")
                self.position -= lost_steps  # The challenging player moves backward
        else:
            if self.language == 'English':
                print(f"{self.name} doesn't have enough coins to challenge.")
            elif self.language == 'Spanish':
                print(f"{self.name} no tiene suficientes monedas para desafiar.")

    def has_won(self):
        return self.position >= 12


language_choice = input("Choose your language / Elige tu idioma [E]nglish / [S]panish: ").lower()

if language_choice == 'e':
    lang = 'English'
elif language_choice == 's':
    lang = 'Spanish'
else:
    print("Invalid choice. Defaulting to English.")
    lang = 'English'

players = [Player(f"Player {i + 1}", lang) for i in range(4)]
turn_count = 0
phantom_awoken = False

while True:
    for player in players:
        if lang == 'English':
            print(f"\n{player.name}'s turn:")
            print(f"Position: {player.position}, Coins: {player.coins}")
        elif lang == 'Spanish':
            print(f"\nTurno de {player.name}:")
            print(f"Posición: {player.position}, Monedas: {player.coins}")

        # Every 3 turns, announce the phantom has awoken
        if turn_count % 3 == 0 and not phantom_awoken:
            if lang == 'English':
                print("\nThe phantom has awoken! A random card challenge appears!")
            elif lang == 'Spanish':
                print("\n¡El fantasma ha despertado! ¡Aparece un desafío aleatorio con carta!")
            phantom_awoken = True

        while True:
            if lang == 'English':
                action = input("Choose action: [m]ove or [c]hallenge: ").lower()
            elif lang == 'Spanish':
                action = input("Elige acción: [m]over o [d]esafiar: ").lower()

            if action == 'm':
                player.move()
                if player.has_won():
                    if lang == 'English':
                        print(f"\nCongratulations! {player.name} has reached the center of the board and won!")
                    elif lang == 'Spanish':
                        print(f"\n¡Felicidades! ¡{player.name} ha alcanzado el centro del tablero y ha ganado!")
                    exit()  # exit the program after winning
                break  # break out of action loop after valid move
            elif action == 'c' or action == 'd':
                target_player = int(input("Enter player number to challenge (1-4): ")) - 1
                if 0 <= target_player < 4 and target_player != players.index(player):
                    player.challenge(players[target_player])
                    break  # break out of action loop after valid challenge
                else:
                    if lang == 'English':
                        print("Invalid player number. Please enter a number between 1 and 4.")
                    elif lang == 'Spanish':
                        print("Número de jugador inválido. Ingresa un número entre 1 y 4.")
            else:
                if lang == 'English':
                    print("Invalid action. Try again.")
                elif lang == 'Spanish':
                    print("Acción inválida. Intenta de nuevo.")

        # Reset phantom_awoken after handling the random card challenge
        if phantom_awoken:
            phantom_awoken = False

        turn_count += 1