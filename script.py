import json
import datetime
import sys
import os
import shutil

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
    mood_dict = {0 :'None',
                 1 :'Stationary',
                 2 :'Eating',
                 3 :'Walking',
                 4 :'Running',
                 5 :'Biking',
                 6 :'Automotive',
                 7 :'Flying'}
                 
    mood = '\nmood - ' + mood_dict[data['mood']]
    weather = '\nweather - ' + str(data['weather'])
    photos = '\n[attached photos](' + str(data['photos']) +')'

    # construct the output list
    if data['photos']:
        output = [dateText, text, photos, '\n---', mood]
    else:
        output = [dateText, text, '\n---', mood]
    if not data['weather']['id'] == -1:
        output.append(weather)

    for itm in output:
        fname = outFname + '.md'
        with open(os.path.join('output', fname), 'a') as ofile:
            print(itm, file=ofile)

    if data['photos']:
        photoname = data['photos'][0]
        shutil.copyfile(photoname,os.path.join('output',photoname))
