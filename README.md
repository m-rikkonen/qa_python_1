# qa_python_1

В проекте решены 5 заданий, каждое в отдельном файле: 
задание 1 - task_1, задание 2 - task_2  и т.д.  

## Задание 1.
Напиши функцию, которая переворачивает число. 
Например: 12 >>> 21, 809 >>> 908. 

Нужно выполнить условия:
* число может быть любой длины,
* число не оканчивается на ноль,
* функция возвращает число.

## Задание 2.
Напиши обработчик для любой строки, которая состоит из слов и знаков препинания. 
Он должен создавать два пустых списка и наполнять их:
* словами из этой строки, включая цифры;
* знаками препинания из этой строки.

Тестовая цитата соответствует ряду условий:
* Подряд идёт только один знак препинания.
* Каждое предложение всегда заканчивается знаком препинания.
* Разделитель между словами — один пробел.

К результату обработки требования такие:
* Значения в списке идут по порядку и не повторяются.
* Одинаковые слова, которые начинаются с маленькой и заглавной букв, — это разные слова. Например, «Мне» и «мне» — разные слова.
 
Импортировать и использовать дополнительные библиотеки и функции не нужно.
Задача решается без регулярных выражений.

## Задание 3.
Над каждым файлом можно производить операции:
* запись — W
* чтение — R
* запуск — X

Напиши функцию, которая обрабатывает действия с файлами.
В словаре *files* ключ — это имя файла, а значение — список из операций, которые доступны для этого файла.
Функция принимает на вход один запрос в виде строки — например, *'write cool_movie.avi'* — и возвращает *OK* или *Access denied*.

## Задание 4.
   В словаре *types* хранятся типы багов. Его ключи — числа от 1 до 5, а значения — от 'Блокирующий' до 'Тривиальный' соответственно.  
   В словаре *tickets* хранятся тикеты (задачи), которые заведены на эти баги. Ключи — числовое значение критичности от 1 до 5, а значения — список с тикетами, которые этим значениям критичности соответствуют. Но некоторые тикеты добавлены несколько раз в разные списки.  
   Составь итоговый словарь, где ключи — это значение критичности, например, 'Значительный', а значения — списки с уникальными тикетами.  

   Для этого напиши две функции:
   * одна удаляет дубли из списков с тикетами,
   * вторая связывает уровень критичности со списком уникальных тикетов.

   Если тикет есть в одном списке, то он уже не может быть в списках на уровень ниже.  

## Задание 5.
Реализуй класс *TestCase*, в котором будут:
* Конструктор, внутри которого устанавливаются атрибуты:
  * *id* тест-кейса — рандомное трёхзначное число;
  * *name* название тест-кейса — передаётся при создании объекта TestCase;
  * *steps* — словарь, куда будут добавляться шаги тест-кейса;
  * *result* — ожидаемый результат тест-кейса.
* Метод *set_step* — добавляет в словарь *steps* шаг тест-кейса. Принимает два параметра: *step_number* и *step_text*. Ключ — это *step_number* (номер шага), а значение — *step_text* (текстовое описание шага).
* Метод *delete_step* — удаляет шаг из *steps* по переданному в метод ключу *step_number*.
* Метод *get_steps* — возвращает текущий список шагов.
* Метод *set_result* — устанавливает ожидаемый результат в атрибут *result* по переданному параметру *result*.
* Метод *get_test_case* — печатает текущее состояние тест-кейса.
