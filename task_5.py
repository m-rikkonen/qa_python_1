import random as r

class TestCase():

    def __init__(self, name, steps ={}):
        self.id = r.randint(100,999)
        self.name = name
        self.steps = steps={}
        self.result = ''


    def set_step(self, step_number, step_text):
        self.steps[step_number] = (step_text)

    def delete_step(self, step_number):
        if step_number in self.steps:
            self.steps.pop(step_number)
        else:
            print('Шага №' + str(step_number) + ' нет в тест-кейсе.')

    def get_steps(self):
        print('Шаги: ', self.steps)

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        print('id: ' + str(self.id))
        print('Наименование: ' + self.name)
        print('Шаги:',  self.steps)
        print('Ожидаемый результат: ' + self.result)














