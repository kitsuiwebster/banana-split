import math

my_file = 'server.txt'
max_lines_per_file = 50000000
file_count = 1
line_count = 0
print(""" 
 ____                                  ____        _ _ _     _ 
| __ )  __ _ _ __   __ _ _ __   __ _  / ___| _ __ | (_) |_  | |
|  _ \ / _` | '_ \ / _` | '_ \ / _` | \___ \| '_ \| | | __| | |
| |_) | (_| | | | | (_| | | | | (_| |  ___) | |_) | | | |_  |_|
|____/ \__,_|_| |_|\__,_|_| |_|\__,_| |____/| .__/|_|_|\__| (_)
                                            |_|                
""")
with open(my_file, 'r') as text_file:
    hold_new_lines = []
    for line in text_file:
        hold_new_lines.append(line)
        line_count += 1

        if line_count == max_lines_per_file:
            file_name = f"server{file_count}.txt"
            with open(file_name, 'a') as next_file:
                next_file.writelines(hold_new_lines)
            hold_new_lines = []
            line_count = 0
            file_count += 1

    if hold_new_lines:
        file_name = f"server{file_count}.txt"
        with open(file_name, 'a') as next_file:
            next_file.writelines(hold_new_lines)

# Calculate the number of files created
total_lines = line_count + (max_lines_per_file * (file_count - 1))
number_of_files = math.ceil(total_lines / max_lines_per_file)

print(f"Number of files created: {number_of_files}")

