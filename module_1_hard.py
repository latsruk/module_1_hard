grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
# print(sorted_students)
# midle_grades = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[-1])/len(grades[-1])]
# print(midle_grades)
# my_dict = dict(zip(sorted_students,midle_grades))
# print(my_dict)
my_dict = {sorted_students[0]: sum(grades[0]) / len(grades[0]),
           sorted_students[1]: sum(grades[1]) / len(grades[1]),
           sorted_students[2]: sum(grades[2]) / len(grades[2]),
           sorted_students[3]: sum(grades[3]) / len(grades[3]),
           sorted_students[4]: sum(grades[4]) / len(grades[4])}
print(my_dict)
