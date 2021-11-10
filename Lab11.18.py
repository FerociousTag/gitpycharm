#zachary blackwell 1941472

list_integers = []
integers = input()
list_integers = integers.split()

display_list = []

length_list = len(list_integers)
#Loop that takes each postion in the list of integers and tests if it is negative
for i in range(0, length_list):
    each_number = int(list_integers[i])
    if each_number >= 0:
        display_list.append(each_number)
#sorts the negative numbers from smallest to largest
display_list.sort(reverse=False)
string_list = [str(i) for i in display_list]
string_list = ' '.join(string_list)
print(string_list, end=' ')