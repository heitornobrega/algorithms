def quick_sort_string(string):
    if len(string) <= 1:
        return string
    pivot = string[0]
    left = ""
    right = ""
    for letter in string[1:]:
        if letter < pivot:
            left += letter
        else:
            right += letter
    return quick_sort_string(left) + pivot + quick_sort_string(right)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string = quick_sort_string(first_string)
    second_string = quick_sort_string(second_string)
    if len(first_string) == 0 and len(second_string) == 0:
        condition = False
    else:
        condition = first_string == second_string
    return (first_string, second_string, condition)
