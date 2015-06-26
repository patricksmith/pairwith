from optparse import OptionParser
import os


PAIRS_FILE = os.path.expanduser('~/.pairs')
CURRENT_PAIR_FILE = os.path.expanduser('~/.current_pair')


def get_available_pairs():
    if not os.path.isfile(PAIRS_FILE):
        return 
    with open(PAIRS_FILE, 'r') as f:
        for line in f:
            yield line.split(',')


def print_available_pairs():
    print 'Available pairs:'
    for pair in get_available_pairs():
        print '\t{}'.format(','.join(pair))


def add_new_pair():
    nickname = raw_input('Enter nickname: ')
    name = raw_input('Enter full name: ')
    email = raw_input('Enter email: ')
    with open(PAIRS_FILE, 'a+') as f:
        f.write(','.join([nickname, name, email]))


def write_current_pair(pair):
    with open(CURRENT_PAIR_FILE, 'w+') as f:
        f.write('{name} <{email}>'.format(name=pair[1], email=pair[2]))


def set_current_pair(pair_name):
    for pair in get_available_pairs():
        if pair[0] == pair_name:
            write_current_pair(pair)


def main():
    parser = OptionParser()
    parser.add_option('-l', '--list', dest='list', default=False, 
        action='store_true', help='List available pairs')
    parser.add_option('-a', '--add', dest='add', default=False,
        action='store_true', help='Add available pair')
    (option, args) = parser.parse_args()

    if option.list:
        print_available_pairs()
    elif option.add:
        add_new_pair()
    elif args:
        set_current_pair(args[0])
