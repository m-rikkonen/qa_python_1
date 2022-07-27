
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

def deletes_duplicates_tickets(tickets):
    t = list(tickets.values())
    t1 = []
    for i in range(len(t)):
        t1 += t[i]
    uniq = list(set(t1))

    for i in tickets:
        tickets[i] = list(set(tickets[i]) & set(uniq))
        uniq = list(set(uniq) ^ set(tickets[i]))


def make_a_dictionary(types, tickets):
    key = list(types.values())
    value = list(tickets.values())
    for i in range(len(key)):
        tickets_by_type[key[i]] = value[i]


deletes_duplicates_tickets(tickets=tickets)
make_a_dictionary(types=types, tickets=tickets)

print(tickets_by_type)

