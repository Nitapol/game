import pandas
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import time

words_data_set = pandas.DataFrame({'keywords':['wlmart womens book set','microsoft fish sauce','books from walmat store','mens login for facebook fools','mens login for facbook fools','login for twetter boy','apples from cook']})

company_name_list = ['walmart','microsoft','facebook','twitter','amazon','apple']

print(len(words_data_set),'....rows')
start_time = time.time()


fuzzed_data_final = pandas.DataFrame()
for s in words_data_set.keywords.tolist():

   step1 = words_data_set[words_data_set.keywords == s]
   step1['keywords2'] = step1.keywords.str.split()
   step2 = step1.keywords2.values.tolist()
   step3 = [item for sublist in step2 for item in sublist]
   step3 = pandas.DataFrame(step3)
   step3.columns = ['search_words']
   step3['keywords'] = s


   fuzzed_data = pandas.DataFrame()
   for w in step3.search_words.tolist():
       step4 = step3[step3.search_words == w]
       step5 = pandas.DataFrame(process.extract(w,company_name_list))
       step5.columns = ['w','score']
       if step5.score.max() >= 90:
           w = ''
       else:
           w

       step4['search_words'] = w
       fuzzed_data = fuzzed_data.append(step4)
   fuzzed_data_final = fuzzed_data_final.append(fuzzed_data)

print("--- %s seconds ---" % (time.time() - start_time))
print(fuzzed_data_final)
