from icalendar import Calendar, Event
fileName = "myCalendarFile.ics"
myCalendar = open(fileName, "rb")
cal = Calendar.from_ical(myCalendar.read())
for component in cal.walk():
    if component.name == "VEVENT" :
        print(component.get("summary"))
        print(component.get("location"))
        print(component.get("dtstart").dt)
        print(component.get("dtend").dt)
        print(component.get("dtstamp").dt)
        print(component.get("uid"))
        allAttendees = component.get("attendee")
        for thisAttendee in allAttendees :
            print(thisAttendee)
myCalendar.close()