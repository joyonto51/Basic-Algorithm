fist_term = 0
second_term = 1
print(fist_term)
print(second_term)

while(second_term<=1000):
    temp = second_term
    second_term = second_term + fist_term
    fist_term = temp
    print(second_term)