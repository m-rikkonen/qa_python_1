
files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}

dictionary_for_conversion = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}

def actions_with_files(string):

    new_string = string.split()
    file_operation = new_string[0]
    file_name = new_string[1]
    file_action = dictionary_for_conversion[file_operation]

    if file_name in files:
        if file_action in files[file_name]:
             print('OK')
        else:
             print('Access denied')
    else:
        print('Файла нет в списке')


actions_with_files('write cool_movie.avi')
actions_with_files('execute cool_movie.avi')



