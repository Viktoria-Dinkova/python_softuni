# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# •	Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# •	The input always will be valid.

hr_list = {}
while True:
    information = input().split(' -> ')
    if information[0] == 'End':
        for k,v in hr_list.items():
            print(f'{k}')
            for employ_id in v:
                print(f'-- {employ_id}')
        break
    else:
        if information[0] not in hr_list:
            hr_list[information[0]] = [information[1]]
        else:
            if information[1] not in hr_list[information[0]]:
                hr_list[information[0]].append(information[1])
