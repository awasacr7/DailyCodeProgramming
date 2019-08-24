from bisect import bisect_left as bisect
words = ['able', 'abode', 'about', 'above', 'abuse','awanesh','awesome']

def autocomplete(strings,prefix):
    dictionary = [s.lower() for s in sorted(strings)]
    print(dictionary)
    next_prefix = prefix + 'a' if prefix[-1] == 'z' else prefix[:-1] + chr(ord(prefix[-1]) + 1)
    # print(next_prefix,prefix)
    # print(bisect(dictionary, prefix),bisect(dictionary, next_prefix))
    return dictionary[bisect(dictionary, prefix):bisect(dictionary, next_prefix)]

print(autocomplete(words,'abo'))