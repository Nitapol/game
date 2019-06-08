import pandas
from fuzzywuzzy import process
from operator import itemgetter
import time

words_data_set = pandas.DataFrame({
    'keywords': ['wlmart womens book set',
                 'microsoft fish sauce',
                 'books from walmat store',
                 'mens login for facebook fools',
                 'mens login for facbook fools',
                 'login for twetter boy',
                 'apples from cook']})
company_name_list = [
    'walmart', 'microsoft', 'facebook', 'twitter', 'amazon', 'apple']
print(len(words_data_set), '....rows')
start_time = time.time()
fuzzed_data_final = pandas.DataFrame()
for s in words_data_set.keywords.tolist():
    step3 = pandas.DataFrame(s.split())
    step3.columns = ['search_words']
    step3['keywords'] = s

    fuzzed_data = pandas.DataFrame()
    for w in step3.search_words.tolist():
        step4 = step3[step3.search_words == w]
        if max(process.extract(w, company_name_list), key=itemgetter(1))[1] >= 90:
            w = ''
        default = pandas.options.mode.chained_assignment
        pandas.options.mode.chained_assignment = None
        step4['search_words'] = w
        pandas.options.mode.chained_assignment = default
        fuzzed_data = fuzzed_data.append(step4)
    fuzzed_data_final = fuzzed_data_final.append(fuzzed_data)

t = (time.time() - start_time)
print("--- %s seconds ---" % t)
rows = 1
names = 2000
e = t / len(words_data_set) / len(company_name_list) * rows * 1000000. * names
h = e / 3600
d = h / 24
print('Estimation for %d million rows and %d company names: %d seconds or'
      ' %d hours or %d days'
      % (rows, names, e, h, d))
print(fuzzed_data_final)
