for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()
#Since out output is not in formatted correctly Here I am printing the values by formatting the proper numbers so firstprint
# so number 1 is lined with 2 char outputs, square and cube is lined with 4 char output
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::2])