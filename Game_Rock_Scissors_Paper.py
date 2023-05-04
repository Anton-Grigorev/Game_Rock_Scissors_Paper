# Game 'Rock, Scissors, Paper' / Игра "Камень, Ножницы, Бумага"

# Создаем класс игрока
class Player:
    def __init__(self, name):
        self.name = name                            # Имя игрока
        self.choice = None                          # Выбор игрока, пока неопределен

    # Определяем метод запроса выбора игрока
    def choose(self):
        self.choice = input(f"{self.name}, choose rock, paper or scissors: ").lower()

# Создаем класс игры с основными уловиями и условиями победы
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rules = {                              # Описываем основные правила через словарь
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    # Определяем метод выбора победителя
    def get_winner(self):
        if self.player1.choice == self.player2.choice:
            return None                             # Если выборы обоих игроков совпадают, то победителя нет
        elif self.rules[self.player1.choice] == self.player2.choice:
            return self.player1                     # Если выбор игрока1 является ключом в словаре, а 2 - значение, то win 1
        else:
            return self.player2                     # Если выбор игрока2 является ключом в словаре, а 1 - значение, то win 2


    #Определяем метод самой игры
    def play(self):
        choise = ''                                 # объявляем переменную для цикла

        while choise != 'q'.lower():                # обозначаем условия остановки бесконечного цикла
            self.player1.choose()                   # вызываем запрос на выбор игрока1
            self.player2.choose()                   # вызываем запрос на выбор игрока1

            winner = self.get_winner()              # вызываем метод определения победителя

            if winner:                              # печатаем результат
                print(f"{winner.name} победил!")
            else:
                print("У нас ничья.")

            print()                                 # далее запрос на продолжение игры
            choise = input('Continue - "enter"; If quit - enter "q":  ')



# Пример использования и запуска Игры:
player1 = Player("Игрок 1")
player2 = Player("Игрок 2")
game = Game(player1, player2)
game.play()
