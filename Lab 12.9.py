#zachary blackwell 1941472

#creates lists for all of the names and ages
names = []
ages = []
#splits the inout into name and age inputs
name_age = input().split()
name = name_age[0]
age = name_age[1]

#while the name is not name or age is not "-1" this will run
while (name or age) != "-1":
    try:
        age = int(name_age[1]) + 1
    #valueError Exception

    except ValueError:
        age = 0
    names.append(name)
    ages.append(age)
    name_age = input().split()
    name = name_age[0]

for i in range(len(names)):
    print(names[i], ages[i])


