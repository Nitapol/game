import pandas
from fuzzywuzzy import process
import time

lines = [
    'wlmart womens book set', 'microsoft fish sauce',
    'books from walmat store', 'mens login for facebook fools',
    'mens login for facbook fools', 'login for twetter boy',
    'apples from cook'
]
companies = ['walmart', 'microsoft', 'facebook', 'twitter', 'amazon', 'apple']

text = open('/Users/alex/PycharmProjects/war_peace/war_peace.txt', encoding='utf-8')

start_time = time.perf_counter()

keywords = []
search_words = []
dictionary = {}
dictionary2 = {}
line_number = 0
while True:
    line = text.readline()
    # print(line)
    if not line:
        print(line_number)
        break
    line_number += 1
    if line_number % 100 == 0:
        print(line_number)
# for line in lines:
    for word in line.split():
        if word in dictionary2:
            counter = dictionary2[word] + 1
        else:
            counter = 1
        dictionary2[word] = counter
        if word in dictionary:
            score = dictionary[word]
        else:
            match_score_list = process.extractBests(
                word, companies, score_cutoff=90, limit=1)
            score = True if match_score_list else False
            dictionary[word] = score
        keywords.append(line)
        search_words.append('' if score else word)
fuzzed_data_final = pandas.DataFrame(
    {'search_words': pandas.Series(search_words),
     'keywords': pandas.Series(keywords)})
total_time = time.perf_counter() - start_time
print("--- %f seconds ---" % total_time)
rows = 1
names = 2000
e = total_time / len(lines) / len(companies) * rows * 1000000. * names
h = e / 3600
d = h / 24
print('Time estimation for %d million rows and %d company names: %d seconds or'
      ' %d hours or %d days' % (rows, names, e, h, d))
print(fuzzed_data_final)
# lst = dictionary2.items()
lst = [x for x in dictionary2.items()]
lst.sort(key=lambda x: x[1], reverse = True)
print(lst)
