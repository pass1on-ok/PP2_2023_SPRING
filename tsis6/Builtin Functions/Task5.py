def TupleTrue():
    my_tuple = (True, True, False, True)

    if all(my_tuple):
        print("All elements in the tuple are true")
    else:
        print("Not all elements in the tuple are true")


TupleTrue()
