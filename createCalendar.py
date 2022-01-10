from icalendar import Calendar, Event
from datetime import datetime
import pytz
from icalendar import vCalAddress, vText
cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')
event = Event()
event.add('summary', 'Meeting : usage of iCalendar to create ics files')
event.add('dtstart', datetime(2022,1,10,8,0,0,tzinfo=pytz.utc))
event.add('dtend', datetime(2022,1,10,10,0,0,tzinfo=pytz.utc))
event.add('dtstamp', datetime(2022,1,10,0,10,0,tzinfo=pytz.utc))

organizer = vCalAddress('MAILTO:noone@example.com')

organizer.params['cn'] = vText('ALABOUCH Salah-Eddine')
organizer.params['role'] = vText('CHAIR')
event['organizer'] = organizer
event['location'] = vText('Paris, France')
"""
uid : This property specifies the persistent, globally unique identifier for the iCalendar object.
This can be used, for example, to identify duplicate calendar streams that a client may have been given access to.
"""
event['uid'] = '5FC53010-1267-4F8E-BC28-1D7AE55A7C99'
event.add('priority', 5)

attendee = vCalAddress('MAILTO:salaheddine@example.com')
attendee.params['cn'] = vText('ALABOUCH Salah-Eddine')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

attendee = vCalAddress('MAILTO:jeanmcdonald@example.com')
attendee.params['cn'] = vText('Jean McDonald')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

cal.add_component(event)

directory = "myCalendarFile.ics"
f = open(directory, 'wb')
f.write(cal.to_ical())
f.close()