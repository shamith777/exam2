import sys
if len(sys.argv) !=5:
    script_name = sys.argv[0]
    name = sys.argv[1]
    reg_no = sys.argv[2]
    dept = sys.argv[3]
    email = sys.argv[4]
else:
    name = ""
    reg_no = ""
    dept = ""
    email = ""

print("Student Name:",name)
print("Registration Number:",reg_no)
print("Department:",dept)
print("Email ID:",email)
