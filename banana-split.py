# @name: Cawdrey
# @author: kitsuiwebster

import math
from yaspin import yaspin
from yaspin.spinners import Spinners

print("""
                                                                                
   ▒▒▒▒                                                                                   
   ▓▓██▒▒           ____                                  ____        _ _ _     _ 
  ░░██████░░       | __ )  __ _ _ __   __ _ _ __   __ _  / ___| _ __ | (_) |_  | |
  ░░██████░░       |  _ \ / _` | '_ \ / _` | '_ \ / _` | \___ \| '_ \| | | __| | |
    ██████▒▒       | |_) | (_| | | | | (_| | | | | (_| |  ___) | |_) | | | |_  |_|
    ░░▓▓▓▓▓▓       |____/ \__,_|_| |_|\__,_|_| |_|\__,_| |____/| .__/|_|_|\__| (_)
     ░░▓▓▓▓▒▒                                                  |_|                
      ░░▓▓▓▓▒▒                                                                  
        ▓▓▓▓▓▓░░                                                                      ░░▓▓▓▓▓▓
        ▒▒▓▓▓▓▓▓▓▓░░                                                                ▓▓▒▒▓▓▓▓▓▓
        ░░▓▓▓▓▓▓▓▓▒▒▒▒░░                                                        ░░▓▓▓▓▓▓▓▓▓▓▓▓
          ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒                                                  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          ▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░                                          ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒                                  ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░                    ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  
          ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
            ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░    
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒      
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒        
                  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒          
                    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░            
                        ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                
                            ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                    
                                  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒                          

""")
my_file = input("Please enter the name of the file to read: ")
max_lines_per_file = int(input("Please enter the maximum number of lines per file: "))

file_count = 1
line_count = 0

with yaspin(Spinners.simpleDotsScrolling, text="Loading...", color="red") as spinner:
    spinner.start()
    
    with open(my_file, 'r') as text_file:
        hold_new_lines = []
        for line in text_file:
            hold_new_lines.append(line)
            line_count += 1

            if line_count == max_lines_per_file:
                file_name = f"{my_file.split('.')[0]}_{file_count}.txt"
                with open(file_name, 'a') as next_file:
                    next_file.writelines(hold_new_lines)
                hold_new_lines = []
                line_count = 0
                file_count += 1

        if hold_new_lines:
            file_name = f"{my_file.split('.')[0]}_{file_count}.txt"
            with open(file_name, 'a') as next_file:
                next_file.writelines(hold_new_lines)
    
    spinner.stop()

total_lines = line_count + (max_lines_per_file * (file_count - 1))
number_of_files = math.ceil(total_lines / max_lines_per_file)

print(f"Number of files created: {number_of_files}")
