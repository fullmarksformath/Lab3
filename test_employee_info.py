import employee_info
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
# test_get_employees_by_age_range()

def test_employee_info_negative():
    lower_limit=-5
    upper_limit=24
    assert(employee_info.get_employees_by_age_range(lower_limit,upper_limit)==False)

def test_employee_info_positive():
    lower_limit=5
    upper_limit=24
    assert(len(employee_info.get_employees_by_age_range(lower_limit,upper_limit))==1)

def test_employee_info_no_results():
    lower_limit=5
    upper_limit=22
    assert(len(employee_info.get_employees_by_age_range(lower_limit,upper_limit))==0)

# test_calculate_average_salary()

def test_calculate_average_salary():
    assert(employee_info.calculate_average_salary(employee_data)==60166.666666666664)

# get_employees_by_dept()

def test_get_employees_by_dept_valid():
    department='Sales'
    assert(len(employee_info.get_employees_by_dept(department))==2)
