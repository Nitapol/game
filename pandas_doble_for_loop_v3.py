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

start_time = time.perf_counter()

keywords = []
search_words = []
for line in lines:
    line_results = []
    for word in line.split():
        match_score_list = process.extractBests(
            word, companies, score_cutoff=90, limit=1)
        keywords.append(line)
        search_words.append('' if match_score_list else word)
fuzzed_data_final = pandas.DataFrame(
    { 'search_words': pandas.Series(search_words),
      'keywords': pandas.Series(keywords) })

total_time = time.perf_counter() - start_time
print("--- %f seconds ---" % total_time)
rows = 1
names = 2000
e = total_time / len(lines) / len(companies) * rows * 1000000. * names
h = e / 3600
d = h / 24
print('Time estimation for %d million rows and %d company names: %d seconds or'
  ' %d hours or %d days'
  % (rows, names, e, h, d))
print(fuzzed_data_final)
