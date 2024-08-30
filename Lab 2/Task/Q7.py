def temperature(temps):
    average_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    temp_sorted = sorted(temps)

    print(f"Average Temperature recorded: {average_temp}")
    print(f"Highest Temperature: {max_temp}")
    print(f"Lowest Temperature: {min_temp}")
    print(f"Sorted list of Temperatures: {temp_sorted}")

temps_list = [30, 35, 28, 40, 36, 31, 29]
temperature(temps_list)
(temps_list.pop(3))
print(f"Temperatures after removing day 4: {temps_list}")


