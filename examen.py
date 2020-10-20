from collections import defaultdict
import string


def read_file(filename):
    '''Функция читает текст файла и делит его по абзацам'''
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        paragraphs = text.split('\n')
    return paragraphs


def index(paragraphs, di):
    '''Функция создает обратные индексы слов'''
    i = -1
    for paragraph in paragraphs:
        i += 1
        for sign in string.punctuation:
            paragraph = paragraph.replace(sign, '')
        words = paragraph.lower().split()
        j = -1
        for word in words:
            j += 1
            di[word].append((i, j))
    return di


def take_words():
    '''Функция принимает слова'''
    word1 = input('Первое слово: ')
    word2 = input('Второе слово: ')
    return word1, word2


def find_words(word1, word2, di):
    '''Функция проверяет, находятся ли слова в одном абзаце.
    А также считает расстояние между словами, если они находятся в одном абзаце'''
    indeces1 = di[word1]
    indeces2 = di[word2]
    dif = 0
    res = False
    for i in indeces1:
        for j in indeces2:
            if i[0] == j[0]+1 or i[0] == j[0]-1:  # Проверяем, находятся ли слова в соседних абзацах
                res = True
            elif i[0] == j[0]:  # Проверяем, находятся ли слова в одном абзаце
                if j[1] - i[1] > 0:  # Находим положительную разницу между словами
                    if dif == 0 or dif > j[1] - i[1]:  # Берем наименьшее расстояние
                        dif = j[1] - i[1]
                else:
                    if dif == 0 or dif > i[1] - j[1]:
                        dif = i[1] - j[1]
    if not res:
        res = False
    if dif == 0:
        dif = False
    return res, dif


def main():
    parags = read_file('first_chapter.txt')
    reversed_index = defaultdict(list)
    reversed_index = index(parags, reversed_index)
    word1, word2 = take_words()
    res, dif = find_words(word1, word2, reversed_index)
    print(f'В соседних абхацах: {res}')
    if dif:
        print(f'Расстояние между словами в одном абзаце: {dif}')


if __name__ == '__main__':
    main()
