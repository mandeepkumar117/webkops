numbers = [2, 1, 5, 1, 3, 2]

window_size = 3

window_sum = 0

for i in range(window_size):
    window_sum = window_sum + numbers[i]

maximum = window_sum

for i in range(window_size, len(numbers)):
    window_sum = window_sum - numbers[i - window_size]
    window_sum = window_sum + numbers[i]

    if window_sum > maximum:
        maximum = window_sum

print("Maximum sum:", maximum)