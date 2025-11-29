import sys
if len(sys.argv) !=5:
    script_name = sys.argv[0]
    name = sys.argv[1]
    reg_no = sys.argv[2]
    dept = sys.argv[3]
    email = sys.argv[4]
else:
    Name = "Shamith"
    Reg_no = 272
    Dept = "BCA"
    Email = "shamithramdurg302@gmail.com"

print("Student Name:",Name)
print("Registration Number:",Reg_no)
print("Department:",Dept)
print("Email ID:",Email)
