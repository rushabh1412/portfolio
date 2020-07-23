charlist="abcdefghijklmnopqrstuvwxyz,ABCDEFGHIJKLMNOPQRSTUVWXYZ.1234567890!@#$%&*"
password="B2#W0lveR1ne"

# charlist="abcdefghijklmnopqrstuvwxyz"
# password="passw"


for current in range(5):
    a=[i for i in charlist]
    for x in range(current):
        a=[y + i for i in charlist for y in a]
        if password in a:
            print(f"password is: {a[a.index(password)]}")
            exit()
