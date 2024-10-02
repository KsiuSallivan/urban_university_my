class WordsFinder:
    """Объект этого класса должен принимать при создании неограниченного количество названий файлов
    и записывать их в атрибут file_names в виде списка или кортежа"""

    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        """подготовительный метод, который возвращает словарь"""

        all_words = {}

        for fl in self.file_names:
            with open(fl, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line1 = line.replace(',', '')
                    line2 = line1.replace('.', '')
                    line3 = line2.replace('=', '')
                    line4 = line3.replace('!', '')
                    line5 = line4.replace('?', '')
                    line6 = line5.replace(';', '')
                    line7 = line6.replace(':', '')
                    line8 = line7.replace(' - ', '')

                    string_clear = line8.split(' ')
                all_words[fl] = string_clear

        return all_words

    def find(self, word):
        """Метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла."""
        find_dist = {}
        word = word.lower()
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                find_dist[name] = words.index(word) + 1

        return find_dist

    def count(self, word):
        """метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - количество слова word в списке слов этого файла."""
        count_dist = {}
        word = word.lower()
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                count_dist[name] = words.count(word)

        return count_dist


# test
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
