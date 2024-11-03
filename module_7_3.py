class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    for p in punctuation:
                        content = content.replace(p, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words
    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        search_word = word.lower()
        for name, words in all_words.items():
            try:
                position = words.index(search_word)
                result[name] = position
            except ValueError:
                result[name] = -1
        return result
    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        search_word = word.lower()
        for name, words in all_words.items():
            count = words.count(search_word)
            result[name] = count
        return result

finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))  #
print(finder.count('teXT'))