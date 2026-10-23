def max_number(a,b):
    if a>b:
        return a
    else:
        return b

def empty_function():
    pass

def even_numbers(n):
    for i in range(n):
        if i%2==0:
            yield i

def test_max_number():
    assert max_number(1,2) == 2
    assert max_number(3,2) == 3
    assert max_number(5,5) == 5
    assert max_number(-1,-5) == -1
    assert max_number(0,0) == 0
    assert max_number(5,-11) == 5

test_max_number()


