pw = "admin123"
i = 1
check = 0
while i <= 3:
    a = input("Enter password: ")
    if a == pw:
        print("Access Granted")
        check = 1
        break
    i += 1
if check == 0:
    print("Access Denied")
