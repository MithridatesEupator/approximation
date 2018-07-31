from math import pi, e as euler_num




def approx(equation, round_digits, expectation, deviation, tri_x, start_x=None, end_x=None):
    if start_x is None or start_x is "n_infinity":
        start = expectation - (deviation * 5)
    else:
        start = start_x - expectation
    if end_x is None or end_x is "infinity":
        end = expectation + (deviation * 5)
    else:
        end = end_x - expectation
    incrementer = expectation
    final_l = 0
    final_r = 0
    while incrementer < abs(end):
        final_r += tri_x * equation(expectation, deviation, incrementer)
        incrementer += tri_x
    incrementer = expectation
    while incrementer < abs(start):
        final_l += tri_x * equation(expectation, deviation, incrementer)
        incrementer += tri_x
    if (start > expectation):
        final_l = -1 * final_l
    if (end < expectation):
        final_r = final_r * -1
    final = final_l + final_r
    final = round(final, round_digits)
    return final

f = lambda expectation, deviation, x: ((deviation * (2 * pi) ** .5) ** -1) * euler_num ** (-1 * (((x - expectation) ** 2) / (float(2 * (deviation ** 2)))))

print(approx(f, 4, 0, 1, .0001, -1, 0))