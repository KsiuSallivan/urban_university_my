import unittest
from module_12_3_frozen_freezing_cases import skip_if_frozen


# классы для тестирования
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# unit test
class TournamentTest(unittest.TestCase):
    all_results = []
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            # Форматируем вывод, используя метод __str__ для объектов Runner
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(formatted_result)

    @skip_if_frozen
    def test_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertEqual(list(result.values())[-1], self.runner3)

    @skip_if_frozen
    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertEqual(list(result.values())[-1], self.runner3)

    @skip_if_frozen
    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)  # Порядок участников
        result = tournament.start()
        self.all_results.append(result)
        self.assertEqual(list(result.values())[-1], self.runner3)


if __name__ == '__main__':
    unittest.main()