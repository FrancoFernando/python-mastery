def catch_all_unpacking():

    
    student_ages = [20, 29, 24, 18, 27, 20, 19, 21, 36, 33]
    student_ages_descending = sorted(student_ages, reverse=True)
    
    # catch all unpacking
    oldest, second_oldest, *others = student_ages_descending
    print(oldest, second_oldest, others)
    # 36 33 [29, 27, 24, 21, 20, 20, 19, 18]
    oldest, *others, youngest = student_ages_descending
    print(oldest, youngest, others)
    # 36 18 [33, 29, 27, 24, 21, 20, 20, 19]
    *others, second_youngest, youngest = student_ages_descending
    print(youngest, second_youngest, others)
    # 18 19 [36, 33, 29, 27, 24, 21, 20, 20]

    # slicing and indexing
    oldest = student_ages_descending[0]
    second_oldest = student_ages_descending[1]
    others = student_ages_descending[2:]
    print(oldest, second_oldest, others)