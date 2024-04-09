"""
Задание: Разработать консольную игру "Битва героев" на Python
с использованием классов и разработать план проекта по этапам/или
создать kanban доску для работы над данным проектом
Общее описание:
Создайте простую текстовую боевую игру, где игрок и компьютер
управляют героями с различными характеристиками.
Игра состоит из раундов, в каждом раунде игроки по очереди
наносят урон друг другу, пока у одного из героев не закончится здоровье.

"""
import random


class Hero:
    def __init__(self, name):
        """ Инициализатор класса с атрибутами """
        self.name = name        # Имя героя
        self.health = 100       # Здоровье героя
        self.attack_power = 20  # Сила атаки героя

    def attack(self, other):
        """
        Атака на другого героя с нанесением ему урона
        other: другой герой (объект класса Hero)
        """

        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} единиц урона.")

    def is_alive(self):
        """ Проверка состояния героя"""
        return self.health > 0


class Game:
    def __init__(self):
        """ Имена героев"""
        self.player = Hero(input("Введите имя вашего героя: "))
        self.computer = Hero("Компьютерный герой")

    def start(self):
        current_turn = 0  # 0 для игрока, 1 для компьютера
        # пока здоровье позволяет
        while self.player.is_alive() and self.computer.is_alive():
            print(
                f"\nЗдоровье {self.player.name}: {self.player.health} единиц, Здоровье {self.computer.name}: {self.computer.health} единиц")
            if current_turn == 0:
                self.player.attack(self.computer)
                current_turn = 1
            else:
                self.computer.attack(self.player)
                current_turn = 0

            # Добавление случайности в силу удара
            self.player.attack_power = random.randint(15, 25)
            self.computer.attack_power = random.randint(15, 25)

        if self.player.is_alive():
            winner = self.player.name
        else:
            winner = self.computer.name

        print(f"\nИгра окончена. Победил {winner}!")


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
