
def find_common_participants(participants_first_group, participants_second_group,q=','):
    a= participants_first_group.split(q)
    b= participants_second_group.split(q)
    c=list(set(a).intersection(b))
    c.sort()
    return c

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,'|'))