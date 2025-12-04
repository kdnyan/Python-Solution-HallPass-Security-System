
# list_of_students_out = ["Tommy","Andy","Sebastian","Allen", "Ben"]

# list_of_time_out = ["7","4","3","6","20"]
# time = zip(list_of_students_out, list_of_time_out)
# print (time)
# if time < (5):
#  print("You are safe")
# if time in range(6,10):
#     print("You have been flagged for being out for an unnecessary amount of time.")
# if time in range(11,60):
#    print ("You ahve been flagged for being out for an unnecessary amount of time.")



# if list_of_time_out > five:
#     print(warning)
# print(list)

# time = dict(zip(list_of_students_out), list_of_time_out)

# moods = dict(zip(list1, list2))

list_of_students_out = ["Tommy","Andy","Sebastian","Allen", "Ben"]

list_of_time_out = [7,4,3,6,20]

# Create a dictionary: {student: minutes_out}
time_out_dict = dict(zip(list_of_students_out, list_of_time_out))
print(time_out_dict)

# Loop through each student and their time
for student, minutes in time_out_dict.items():

    if minutes < 5:
        print(f"{student}: You are safe.")

    elif 5 <= minutes < 10:
        print(f"{student}: You have been flagged for being out unnecessarily.")

    elif 10 <= minutes < 60:
        print(f"{student}: You have been flagged for being out for a long time.")

    else:
        print(f"{student}: EXTREME time out. Further conversation needed.")
