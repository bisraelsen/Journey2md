import json
import datetime
import sys
import os

in_folder = 'journey-test/'
files = os.listdir(in_folder)

for entry in files:

    with open(os.path.join(in_folder, entry)) as data_file:
        data = json.load(data_file)

    date = data['date_journal']
    dateobj = datetime.datetime.fromtimestamp(date/1000)
    dateText = '# ' + dateobj.strftime('%A, %d %B %Y -- %H:%M:%S')

    outFname = dateobj.strftime('%d%m%Y_%H%M%S')

    text = '\n' + str(data['text'])

    # TODO: Convert mood to text values
    mood = '\nmood - ' + str(data['mood'])
    weather = '\nweather - ' + str(data['weather'])
    photos = '\nattached photos - ' + str(data['photos'])

    # construct the output list
    output = [dateText, text, '\n---', mood]
    if not data['weather']['id'] == -1:
        output.append(weather)
    if data['photos']:
        output.append(photos)

    for itm in output:
        fname = outFname + '.md'
        with open(os.path.join('output', fname), 'a') as ofile:
            print(itm, file=ofile)
