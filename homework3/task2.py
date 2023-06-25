# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
import re

text = 'This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. ' \
       'It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, ' \
       'so the tutorial can be read off-line as well. For a description of standard objects and modules, ' \
       'see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. ' \
       'To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. ' \
       'There are also several books covering Python in depth.'

text_cleaned = re.sub(r'[^\w\s]', '', text.lower())
word_count = {}
for i in text_cleaned.split(' '):
    word_count[i] = text_cleaned.count(i)


print(sorted(word_count.values())[::-1][:10])