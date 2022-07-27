types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {}

def make_a_dictionary(types, tickets):
    key = list(types.values())
    value = list(tickets.values())
    for i in range(len(key)):
        tickets_by_type[key[i]] = value[i]

def deletes_duplicates_tickets(tickets):
    uniq = []
    tickets_uniq = {}

    for i in tickets:
        for j in tickets[i]:
            if j not in uniq:
                uniq.append(j)

    for i in tickets:
        for j in tickets[i]:
            if j in uniq:
                key = i
                value = j
                if key not in tickets_uniq:
                    tickets_uniq[key] = [value]
                else:
                    tickets_uniq[key].append(value)
                uniq.remove(j)

    make_a_dictionary(types=types, tickets=tickets_uniq)


deletes_duplicates_tickets(tickets=tickets)
print(tickets_by_type)






