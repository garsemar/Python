cam3 = ("""\
   _________
  /___   ___\
 //@@@\ /@@@\\
 \\@@@/ \@@@//
  \___ " ___/
     | - |
      \_/
""")
cam5 = ("""\
    o   o
     )-(
    (O O)
     \=/
    .-"-.
   //\ /\\
 _// / \ \\_
=./ {,-.} \.=
    || ||
    || ||
  __|| ||__ 
 `---" "---'
""")
si = 0
num = 0
while True:
    num = [int(num) for num in input().split(" ")]
    for i in num:
        if i == -1:
            si = 1
            num.remove(i)
    if int(si) == 1:
        break
print(num)
for j in num:
    if j == 3:
        print(cam3)
    elif j == 5:
        print(cam5)
