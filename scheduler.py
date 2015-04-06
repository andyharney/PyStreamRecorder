__author__ = 'Andy'


def init():
    print('\n1. Display Schedule\n2. Add Item to Schedule\n3. Clear Schedule\n9. Quit\n')
    choice = 0
    while True:
        try:
            choice = int(input('Choose Option - '))
            break
        except ValueError:
            print('\nChoose Valid Option\n')
    if choice == 1:
        read_schedule()
    if choice == 2:
        print('Enter New Schedule Item\nStart Time {0} - Stop Time {0} - Station (R2/R4)\n'.format('(HHMMSS)'))
        item = input('--> ')
        it_list = item.split(' ')
        item = ','.join(it_list)
        write_schedule(item)
    if choice == 3:
        print('Not Yet')
        init()
    if choice == 9:
        exit(1)


def read_schedule():
    import os

    if os.path.isfile('schedule.txt'):
        with open('schedule.txt', 'r') as schedule_file:
            items = schedule_file.readlines()
        for item in items:
            arr = item.split(',')
            print('\nStart Time : {0} - Stop Time : {1} - Station : {2}'.format(arr[0], arr[1], arr[2]))
        init()
    else:
        print('No Schedule')
        init()


def write_schedule(new_item):
    import os

    if os.path.isfile('schedule.txt'):
        with open('schedule.txt', 'a') as schedule_file:
            schedule_file.write(new_item)
            schedule_file.close()
        init()
    else:
        with open('schedule.txt', 'w') as schedule_file:
            schedule_file.write(new_item)
            schedule_file.close()
        init()

init()