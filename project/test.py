import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday)
print()

print(calendar.calendar(2022))

calendar.weekday = day_of_the_week = (input("what is the day today? "))
if (calendar.weekday) == "monday" :
    print("good morning!It's Monday, drink some coffee and get ready for work!")
elif (calendar.weekday) == "tuesday" :
    print("hello!It's Tuesday,i hope you have a great day.Make sure to stay healthy and happy.")
elif (calendar.weekday) == "wednesday" :
    print("hi!It's a great wednesday outside,have some fun at work and make sure to relax when you are home")
elif (calendar.weekday) == "thursday" :
    print("hey! What's up? What a lovely day outside! Have a great thursday at work and have some rest when you get home")
elif (calendar.weekday) == "friday" :
    print("wakey wakey,rise and shine! It's friday,how have you been? Time to drink your morning coffee and go to work")
elif (calendar.weekday) == "saturday" :
    print("hiya! What's good? It's saturday, your weekend! Have a good rest from all that work and relax at a restaurant or a cafe")
elif (calendar.weekday) == "sunday" :
    print("Howdy pal, have a great sunday and relax at the beach or play in the rain maybe.")