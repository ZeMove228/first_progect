lst = ['1', '2', '3']
int_lst = []


for number in lst:
    int_lst.append(int(number))
print(lst)
print(int_lst)


#_________________________________________
gen_lst = [int(number) for number in lst]
print(gen_lst)



map_lst = map(int, lst)
print(list(map_lst))



names = ['dior', 'misha', 'sankar']


map_names = map(str.capitalize, names)
print(names)
print(list(map_names))

def double_number(number: int):
    return number ** 2

lst  = [11, 22, 44, 55, 66, 12]

map_lst = map(double_number, lst)
print(list(map_lst))

words = ['purple', 'yelow', 'black', 'nokia', 'not', 'ton', 'coin', 'aranmutan']


less_5 = []
more_5 = []


for word in words:
    if len(word) <= 5:
        less_5.append(word)
    else:
        more_5.append(word)

print(less_5)
print(more_5)



def filter_less_5(word: str):
    return len(word) <= 5



filter_list = filter(filter_less_5, words)

print(list(filter_list))


words = ['apple', 'align', 'alive', 'assambler', 'applications',
         'byd', 'banana']


def words_a(word: str):
    return word.startswith('a')


def words_b(word: str):
    return word.startswith('b')

filtered_a = filter(words_a, words)
print(list(filtered_a))


filtered_b = filter(words_b, words)
print(list(filtered_b))






