def max_number(a, b):
    max_int = None
    try:
        if a > b:
            max_int = a
        else:
            max_int = b
    except TypeError:
        print("[max_number] - Это не те типы, которые нам нужны...")
    else:
        print(f"[max_number]: большее {max_int}")
        return max_int
    finally:
        pass


def empty_function():
    pass


def even_numbers(n):
    try:
        for i in range(n):
            if i % 2 == 0:
                yield i
    except TypeError:
        print("[even_numbers] Ошибка типов")
    finally: pass


def test_max_number():
    assert max_number(1, 2) == 2
    assert max_number(3, 2) == 3
    assert max_number(5, 5) == 5
    assert max_number(-1, -5) == -1


print(max_number(4, 6))
print(max_number("f", 6))

print(list(even_numbers(10)))
print(list(even_numbers("f")))

test_max_number()