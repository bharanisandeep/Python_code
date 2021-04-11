#
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6]) # here we are slicing the string so we pring from 0 to 6 but not including 6. So remeber by Tim "upto but not including"

print(parrot[3:5]) #start sring from position 3 to 6 but not including 6


print(parrot[0:9]) #start string from position 0 to 9 but not including 6
print(parrot[:9]) #start string from position 0 to 9 but not including 6

#Slicing with negative numbers
print(parrot[-4:-2]) #start string from position -4 to -2 but not including -2
print(parrot[-4:12]) #start from position -4 to 12 but dont include 12


#Using a stepin slice
print(parrot[0:6:2]) #print string from 0 to 6 with 2nd position each i.e 0 2 4 6 8 like this
print(parrot[0:6:3]) #print string from 0 to 6 with 3nd position each i.e. 0 3 6

number = "9,123,456,789,012,345,678" ##print string from poistion 1 to end with 2nd position each i.e 0 2 4 6 8 like this
(number[1::4])        ## as there is no value after 1st : and 4 means print 4th poistion value
print()

num = "9,111;222:333 444,555;666"
seperators = num[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in num).split()
print([int(val) for val in values])


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])

days = "Mon,Tue,Wed,Thu,Fri,Sat,Sun"
print(days[::5])