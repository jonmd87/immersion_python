"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. Слова разделяются пробелами.
Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами. Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов.
"""
text = ("adipiscing ame Lorem ame ipsum ame. 2 ame dolor 3 ame si't 6 ame't, "
        "consectetur Lorem adipiscing consectetur ! elit ipsum ( t t")
temp_text = (text.lower().replace("'", " "))
for item in list(temp_text):
    if not item.isalpha() and item != " ":
        temp_text = temp_text.replace(item, "")

lst = list(temp_text.split())
dct = dict.fromkeys(set(lst), 0)

while lst:
    dct[lst.pop(0)] += 1
print(dict(sorted(dct.items(), key=lambda x:x[1], reverse=True)[:10]))