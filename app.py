from os import system

# accepted date formats: rfc2822 (Mon, 3 Jul 2006 17:18:43 +0200) and iso8601 (2006-07-03 17:18:43 +0200)
def get_commit_hash(op1):
    return op1.split(' ')[1]


def draw(dates):
    for date in dates:
        print(date)

        command = 'echo "commit" >> test.txt'
        system(command)  # number of times
        
        command = 'git add -A'
        system(command)
        
        command = 'git commit -m "commit"'
        system(command)
        
        #     command = r'git log -1'
        #     op = check_output(command)
        #     commit_hash = get_commit_hash(op)
        
        command = 'git commit --amend --no-edit --date ' + '\"' + date + '\"'
        # format: "Mon 10 Jan 2019 20:19:19 IST"
        system(command)
