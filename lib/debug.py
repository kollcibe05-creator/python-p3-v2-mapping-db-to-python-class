from __init__ import CONN, CURSOR
from department import Department

import ipdb


def reset_database():
    Department.drop_table()
    Department.create_table()

    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")
    # workers = Department.create("Workers", "Ground")
    # q_a = Department.create("Quality Assurance", "Top Floor")


    # workers.delete()
    # q_a.delete()

reset_database()
ipdb.set_trace()