#Using the function Map, count the number of words that start with ‘S’ in input_list.

input_list=["Snehal", "Ojas", "Shobha", "shweta"]

def count_words_starting_with_s(input_list):
    starting_with_s = map(lambda word: word.startswith('S'), input_list)
    count = sum(map(int, starting_with_s))
    return count

count= count_words_starting_with_s(input_list)
print(count)