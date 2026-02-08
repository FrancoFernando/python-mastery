"""Exercise 13: Printing Tuple Records"""

COUNTRIES = [('Canada', 9984670, 38250000),
             ('Italy', 301340, 59110000),
             ('United Kingdom', 242495, 67220000),
             ('France', 551695, 67390000),
             ('Germany', 357022, 83200000),
             ('Japan', 377975, 125700000),
             ('United States', 9833517, 331900000)
]

def format_sort_records():

    countries_by_name = sorted(COUNTRIES, key=lambda c : c[0])
    output = []
    for country in countries_by_name:
        output.append("{0:14} {1:10,} {2:14,}".format(country[0],country[1],country[2]))

    return "\n".join(output)

print(format_sort_records())