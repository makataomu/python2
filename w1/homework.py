import re

task_num = 1
def print_task():
    global task_num
    print('\ttask', task_num)
    task_num += 1

print_task()
def get_type(obj):
    return type(obj)

obj = object()
print(get_type(obj))

print_task()
def calc_str_len(s):
    return len(s)

print(calc_str_len("hello world"))

print_task()
def check_type(var):
    if isinstance(var, list):
        return "The variable is a list."
    elif isinstance(var, tuple):
        return "The variable is a tuple."
    elif isinstance(var, set):
        return "The variable is a set."
    else:
        return "The variable is not a list, tuple, or set."

print(check_type([1]))

print_task()
def sum_first_n(n):
    return n * (n + 1) // 2

print(sum_first_n(5))

print_task()
def sum_items(lst):
    return sum(lst)

print(sum_items([1, 2, 3, 4]))

print_task()
def solve_expression1(x, y):
    return (x + y) ** 2

print(solve_expression1(4, 3))

print_task()
def break_lines(name, age, address):
    print(name)
    print(age)
    print(address)

break_lines("Saule", 18, "Astana")

print_task()
def area_of_triangle(base, height):
    return 0.5 * base * height

print(area_of_triangle(5, 10))

print_task()
def check_circles(x1, y1, r1, x2, y2, r2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if d + r2 <= r1:
        return "C2 is in C1"
    elif d + r1 <= r2:
        return "C1 is in C2"
    elif d < r1 + r2:
        return "Circumference of C1 and C2 intersect"
    return "C1 and C2 do not overlap"

print(check_circles(5, 6, 4, 8, 7, 9))

print_task()
def beautify(str):
    tabs_order = [0,1,2,2]
    abzacs = str.split('Twinkle')

    for abzac in abzacs[1:]:
        abzac = 'Twinkle'+abzac

        lines = re.split(r"[,\.\!\?]\s(?=[A-Z])", abzac)
        for line, tabs in zip(lines, tabs_order):
            print('\t'*tabs, line)

beautify("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" )

print_task()
def first_and_last(lst):
    return lst[0], lst[-1]

color_list = ["Red", "Green", "White", "Black"]
print(first_and_last(color_list))

print_task()
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

d = {0: 10, 1: 20}
print(add_key_to_dict(d, 2, 30))

print_task()
def create_tuple(lst):
    print(lst[1])
    return tuple(lst)

print(create_tuple([1,2]))

print_task()
def remove_third(numbers):
    index = 2
    while numbers:
        if index >= len(numbers):
            index = index & len(numbers) - 1

        removed = numbers.pop(index)
        print(removed)

remove_third(list(range(1, 11)))

