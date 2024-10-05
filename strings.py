'ITVersity, Inc'
"ITVersity, Inc"
company_name = 'ITVersity, Inc'
print(company_name)
print('ITVersity, Inc')
"ITVersity's Courses"
print("ITVersity's Courses")
print('ITVersity\'s Courses')
print('''HEllo World''')

print('''We can use tripple single quotes or tripple double quotes for multi-line strings.

You can have single quotes or double quotes as part of the strings enclosed in triple single quotes (') or triple double quotes(")''')

msg = 'Hello'
audience = 'World'
print(msg + ' ' + audience)
print('%s %s' % (msg, audience))

orig_msg = '%s %s' % (msg, audience)
print(orig_msg)

print('{} {}'.format(msg, audience))
print('{} {}'.format(audience, msg))
print('{v1} {v2}'.format(v2=audience, v1=msg))
print(f'{msg} {audience}')

print(msg + ' ' + audience)
#print(msg + 2 + audience)
print(f'{msg} 2 {audience}')
