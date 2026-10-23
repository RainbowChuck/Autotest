def can_vote(age, native, disc):
    if age>17 and native == True and not disc:
        return True
    else: return False

print(can_vote(5, True, False))
print(can_vote(18, True, True))
print(can_vote(18, False, True))
print(can_vote(18, True, False))

def num_word(a):
    if a in [1,2,3,4,5]:
        try:
            if a == 1:
                return "One"
            elif a == 2:
                return "Two"
            elif a == 3:
                return "Three"
            elif a == 4:
                return "Four"
            elif a == 5:
                return "Five"
        finally:
            print(a)
    else:
        return "Not a value in 1,2,3,4,5"
print(num_word(5))
print(num_word(6))