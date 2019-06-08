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
fuzzed_data_final = pandas.DataFrame()
lines_results = []


def part0():
    counter = 0
    for line in lines:
        for word in line.split():
            counter += 1
    print('Part 0. Count all words.\n', counter, 'words')


def part1():
    for line in lines:
        line_results = []
        for word in line.split():
            match_score_list = process.extractBests(
                word, companies, score_cutoff=90, limit=1)
            line_results.append(True if match_score_list else False)
        lines_results.append(line_results)
    print('Part 1. Match all words.\n', lines_results)


def part2():
    global fuzzed_data_final
    for i, line in enumerate(lines):
        step3 = pandas.DataFrame(line.split())
        step3.columns = ['search_words']
        step3['keywords'] = line

        fuzzed_data = pandas.DataFrame()
        for j, word in enumerate(line.split()):
            step4 = step3[step3.search_words == word]
            w = word
            if lines_results[i][j]:
                w = ''
            default = pandas.options.mode.chained_assignment
            pandas.options.mode.chained_assignment = None
            step4['search_words'] = w
            pandas.options.mode.chained_assignment = default
            fuzzed_data = fuzzed_data.append(step4)
        fuzzed_data_final = fuzzed_data_final.append(fuzzed_data)
    print('Part 2. Create pandas.DataFrame fuzzed_data_final.\n',
          fuzzed_data_final)

def part3():
    global fuzzed_data_final
    keywords = []
    search_words = []
    for i, line in enumerate(lines):
        for j, word in enumerate(line.split()):
            keywords.append(line)
            search_words.append('' if lines_results[i][j] else  word)
    fuzzed_data_final = pandas.DataFrame({ 'search_words': pandas.Series(search_words), 'keywords': pandas.Series(keywords) })
    print('Part 3. Create pandas.DataFrame fuzzed_data_final.\n',
          fuzzed_data_final)

def execute(f):
    start_time = time.perf_counter()
    f()
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


execute(part0)
execute(part1)
execute(part2)
execute(part3)