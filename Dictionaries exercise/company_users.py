command = input()
companies = {}
while command != "End":
    company, emp_id = command.split(" -> ")
    if company in companies:
        if emp_id not in companies[company]:
            companies[company].append(emp_id)
    else:
        companies[company] = [emp_id]
    command = input()
for company in companies:
    print(company)
    for emp_id in companies[company]:
        print(f"-- {''.join(emp_id)}")
