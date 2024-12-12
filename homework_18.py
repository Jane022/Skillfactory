import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students: # 1 итерация: student = 'Александра'
    students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
            # цикл по предметам
    for class_ in classes: # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
        # выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
    {students_marks[student]}''')


print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
        5. Редактирование оценки ученика по предмету
        6. Редактирование предмета
        7. Редактирование имени ученика
        8. Удаление оценки ученика по предмету
        9. Удаление предмета
        10. Удаление имени ученика
        11. Вывести все оценки для определенного ученика
        12. Вывод среднего балла по каждому предмету по определенному ученику.
''')

while True:
        command = int(input('Введите команду: '))
        if command == 1:
            print('1. Добавить оценку ученика по предмету')
                # считываем имя ученика
            student = input('Введите имя ученика: ')
                # считываем название предмета
            class_ = input('Введите предмет: ')
                # считываем оценку
            mark = int(input('Введите оценку: '))
                # если данные введены верно
            if student in students_marks.keys() and class_ in students_marks[student].keys():
                    # добавляем новую оценку для ученика по предмету
                students_marks[student][class_].append(mark)
                print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                # неверно введены название предмета или имя ученика
            else:
                print('ОШИБКА: неверное имя ученика или название предмета')
        elif command == 2:
            print('2. Вывести средний балл по всем предметам по каждому ученику')
                # цикл по ученикам
            for student in students:
                print(student)
                    # цикл по предметам
                for class_ in classes:
                        # находим сумму оценок по предмету
                    marks_sum = sum(students_marks[student][class_])
                        # находим количество оценок по предмету
                    marks_count = len(students_marks[student][class_])
                        # выводим средний балл по предмету
                    print(f'{class_} - {marks_sum//marks_count}')
                print()
        elif command == 3:
            print('3. Вывести все оценки по всем ученикам')
                # выводим словарь с оценками:
                # цикл по ученикам
            for student in students:
                print(student)
                    # цикл по предметам
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        elif command == 4:
            print('4. Выход из программы')
            break
        elif command == 5:
            print('5. Редактирование оценки ученика по предмету')
            student = input('Введите имя ученика:')
            class_ = input('Введите предмет ученика:')
            old_mark = int(input('Введите оценку, которую надо отредактировать:'))
            new_mark = int(input("Введите новую оценку: "))
            if student in students_marks.keys() and class_ in students_marks[student].keys() and old_mark in students_marks[student][class_]:
                students_marks[student][class_].remove(old_mark)
                students_marks[student][class_].append(new_mark)
                print(f'Оценка ученика {student} по предмету {class_} отредактирована с {old_mark} на {new_mark}. Отредактированный список оценок:\n {students_marks}')
            else:
                print('ОШИБКА: неверное имя ученика, название предмета, либо такой оценки у ученика не существует')
        elif command == 6:
            print('6. Редактирование предмета')
            class_ = input('Введите текущий предмет:')
            new_class = input("Введите новый предмет:")
            if class_ in classes:
                for student in students:
                    students_marks[student][new_class] = students_marks[student][class_]
                    del students_marks[student][class_]
                print(f'Предмет {class_} отредактирован на {new_class}. Отредактированный список:\n {students_marks}')
            else:
                print('ОШИБКА: неверное название предмета')

        elif command == 7:
            print('7. Редактирование имени ученика')
            student = input('Введите имя ученика для редактирования:')
            new_student = input("Введите новое имя ученика:")
            if student in students:
                students_marks[new_student] = students_marks[student]
                del students_marks[student]
                print(f'Имя ученика {student} отредактировано на {new_student}. Отредактированный список:\n {students_marks}')
            else:
                print('ОШИБКА: неверное имя ученика')
        elif command == 8:
            print('8. Удаление оценки ученика по предмету')
            student = input('Введите имя ученика:')
            class_ = input('Введите предмет ученика:')
            mark = int(input('Введите оценку, которую надо удалить:'))
            if student in students_marks.keys() and class_ in students_marks[student].keys() and mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(
                    f'Оценка {mark} ученика {student} по предмету {class_} удалена. Отредактированный список оценок:\n {students_marks}')
            else:
                print('ОШИБКА: неверное имя ученика, название предмета, либо такой оценки у ученика не существует')
        elif command == 9:
            print('9. Удаление предмета')
            class_ = input('Введите текущий предмет:')
            if class_ in classes:
                for student in students:
                    del students_marks[student][class_]
                print(f'Предмет {class_} удален. Отредактированный список:\n {students_marks}')
            else:
                print('ОШИБКА: неверное название предмета')
        elif command == 10:
            print('10. Удаление имени ученика')
            student = input('Введите имя ученика для удаления:')
            if student in students:
                del students_marks[student]
                print(f'Имя ученика {student} удалено. Отредактированный список:\n {students_marks}')
            else:
                print('ОШИБКА: неверное имя ученика')
        elif command == 11:
            print('11. Вывести все оценки для определенного ученика')
            student = input("Введите имя ученика:")
            if student in students_marks.keys():
                print ((students_marks[student]).values())
            else:
                print('ОШИБКА: неверное имя ученика')
        elif command == 12:
            print('12. Вывести средний балл по каждому предмету по определенному ученику.')
            student = input("Введите имя ученика:")
            if student in students_marks.keys():
                for class_ in classes:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    print(f'{class_} - {marks_sum//marks_count}')
            else:
                print('ОШИБКА: неверное имя ученика')









