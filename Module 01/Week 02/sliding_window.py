def max_sliding_window(num_list, k):
    result_sliding_window = []

    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        max_value = window[0]

        for num in window:
            if num > max_value:
                max_value = num

        result_sliding_window.append(max_value)

    return result_sliding_window


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_sliding_window(num_list, k))
