import sys
if len(sys.argv) !=5:
    script_name = sys.argv[0]
    name = sys.argv[1]
    reg_no = sys.argv[2]
    dept = sys.argv[3]
    email = sys.argv[4]
else:
    name = "Shamith"
    reg_no = 272
    dept = "BCA"
    email = "shamithramdurg302@gmail.com"

print("Student Name:",name)
print("Registration Number:",reg_no)
print("Department:",dept)
print("Email ID:",email)
