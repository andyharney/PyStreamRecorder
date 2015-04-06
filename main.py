import time
import datetime

radio2url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p'
radio4url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p'


def init():
    choice = 0
    while True:
        print('Menu\n\n1. Load Schedule\n2. One Off Recording\n9. Quit\n')
        try:
            choice = int(input('Choose Option - '))
            break
        except ValueError:
            print('Pick Valid Option')

    if choice == 1:
        print('Load Scheduler Code\nNot Done Yet\n')
        exit(1)
    if choice == 2:
        oneoffrecording()
    if choice == 9:
        exit(1)


def oneoffrecording():
    while True:
        recordstarttimeinput = input('What Time to Start Recording? HHMMSS - ')
        if not recordstarttimeinput:
            recordstarttimeinput = '000001'
        recordendtimeinput = input('What Time to Stop Recording? HHMMSS - ')
        print('Station to Record?')
        print('1 - Radio 2 (Default)')
        print('2 - Radio 4')
        try:
            stationpick = int(input('Chosen Station - '))
        except ValueError:
            stationpick = 1

        if stationpick == 1:
            station = 'BBC Radio 2'
            stationurl = radio2url
        elif stationpick == 2:
            station = 'BBC Radio 4'
            stationurl = radio4url
        try:
            current_time = time.strftime('%Y %m %d')
            start_time = time.strptime('%s %s' % (current_time,
                                                  recordstarttimeinput),
                                       '%Y %m %d  %H%M%S')
            end_time = time.strptime('%s %s' % (current_time,
                                                recordendtimeinput),
                                     '%Y %m %d  %H%M%S')
            break
        except ValueError:
            print('Time Entered Not Correct. Try Again.')

    recordstream(start_time, end_time, station, stationurl)


# noinspection PyTypeChecker
def recordstream(start, stop, station, stationurl):

    import requests
    print('')
    print('Recording Initialised')
    while True:
        if start <= time.localtime():
            print('Recording Started')
            print('Recording ' + station)
            now = datetime.datetime.strftime(datetime.datetime.now(), '%d %B %Y - %H%M')
            filename = now + ' - ' + station + '.mp3'
            with open(filename, 'wb') as mp3file:
                stream = requests.get(stationurl, stream=True)
                if stream.ok:
                    for chunk in stream.iter_content(10240):
                        if stop >= time.localtime():
                            if chunk:
                                mp3file.write(chunk)
                        else:
                            mp3file.close()
                            print('Recording Stopped')
                            exit(1)
        else:
            time.sleep(2)

init()




