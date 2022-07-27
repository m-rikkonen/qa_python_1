
string = "Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и схватит пулю. " \
         "Думаешь, им буду я? Нет. Это я постучу в дверь."

marks_list = []
word_list = []

string = string.replace(',', ' ,')
string = string.replace('!', ' !')
string = string.replace('.', ' .')
string = string.replace('?', ' ?')
new_string = string.split()

for s in new_string:
    if s in ".,!?":
        if s not in marks_list:
            marks_list.append(s)
    else:
        if s not in word_list:
            word_list.append(s)

print(word_list)
print(marks_list)