# Prototype
# Date formats accepted:
# rfc2822: Mon, 3 Jul 2006 17:18:43 +0200
# iso8601: 2006-07-03 17:18:43 +0200

# os.system() runs the specified command. subprocess module is not required since we aren't capturing any output
from os import system

# the following dates are manually entered as of now (refer issue #1) to form the letters: GK
dates = [
    '2019-08-25 18:00:00 +0530',
    '2019-08-19 18:00:00 +0530',
    '2019-08-07 18:00:00 +0530',
    '2019-08-15 18:00:00 +0530',
    '2019-08-13 18:00:00 +0530',
    '2019-08-23 18:00:00 +0530',
    '2019-08-31 18:00:00 +0530',
    '2019-07-28 18:00:00 +0530',
    '2019-07-29 18:00:00 +0530',
    '2019-07-30 18:00:00 +0530',
    '2019-07-31 18:00:00 +0530',
    '2019-08-01 18:00:00 +0530',
    '2019-08-02 18:00:00 +0530',
    '2019-08-03 18:00:00 +0530',
    '2019-07-14 18:00:00 +0530',
    '2019-07-07 18:00:00 +0530',
    '2019-06-30 18:00:00 +0530',
    '2019-06-23 18:00:00 +0530',
    '2019-06-16 18:00:00 +0530',
    '2019-06-17 18:00:00 +0530',
    '2019-06-18 18:00:00 +0530',
    '2019-06-19 18:00:00 +0530',
    '2019-06-20 18:00:00 +0530',
    '2019-06-21 18:00:00 +0530',
    '2019-06-22 18:00:00 +0530',
    '2019-06-29 18:00:00 +0530',
    '2019-07-20 18:00:00 +0530',
    '2019-07-13 18:00:00 +0530',
    '2019-07-06 18:00:00 +0530',
    '2019-07-19 18:00:00 +0530',
    '2019-07-18 18:00:00 +0530',
    '2019-07-17 18:00:00 +0530',
    '2019-07-10 18:00:00 +0530',
    '2019-07-03 18:00:00 +0530',
]

for date in dates:
    print(date)

    command = 'echo "commit" >> test.txt'  # to the end of file
    system(command)  # number of times

    command = 'git add -A'  # git staging
    system(command)

    command = 'git commit -m "commit"'  # git committing
    system(command)

    command = 'git commit --amend --no-edit --date ' + '\"' + date + '\"'
    # amends current commit (HEAD) to change the commit date from date of execution to "date" in the loop
    system(command)
