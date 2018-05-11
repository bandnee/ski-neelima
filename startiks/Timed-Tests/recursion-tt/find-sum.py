

# Complete the function below.

def csp(arr, start):
    if start == len(arr):
        return [0]
    else:
        int_list = csp(arr, start + 1)
        f_list = []
        for i in int_list:
            f_list.append(arr[start] + i)
            f_list.append(i)
        return f_list


def check_if_sum_possible(arr, k):
    r_arr = csp(arr, 0)
    if k in r_arr:
        return True
    else:
        return False