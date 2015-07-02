from optparse import OptionParser
import os


PAIRS_FILE = os.path.expanduser('~/.pairs')
CURRENT_PAIR_FILE = os.path.expanduser('~/.current_pair')


def get_available_pairs():
    if not os.path.isfile(PAIRS_FILE):
        return
    with open(PAIRS_FILE, 'r') as f:
        for line in f:
            yield [part.strip() for part in line.split(',')]


def print_available_pairs():
    print 'Available pairs:'
    for pair in get_available_pairs():
        print '\t{}'.format(','.join(pair))


def add_new_pair():
    nickname = raw_input('Enter nickname: ')
    name = raw_input('Enter full name: ')
    email = raw_input('Enter email: ')
    with open(PAIRS_FILE, 'a+') as f:
        f.write(','.join([nickname, name, email]) + '\n')


def remove_pair(nickname):
    found_pair = None
    pairs = list(get_available_pairs())
    with open(PAIRS_FILE, 'w') as f:
        for pair in pairs:
            if pair[0] != nickname:
                f.write(','.join(pair) + '\n')
            else:
                found_pair = pair

    if found_pair:
        current = get_current_pair()
        found = '{} <{}>'.format(found_pair[1], found_pair[2])
        if current == found:
            unset_pair()


def unset_pair():
    if not os.path.isfile(CURRENT_PAIR_FILE):
        return
    os.remove(CURRENT_PAIR_FILE)


def write_current_pair(pair):
    with open(CURRENT_PAIR_FILE, 'w+') as f:
        f.write('{name} <{email}>'.format(name=pair[1], email=pair[2]))


def set_current_pair(pair_name):
    unset_pair()
    for pair in get_available_pairs():
        if pair[0] == pair_name:
            write_current_pair(pair)


def get_current_pair():
    if not os.path.isfile(CURRENT_PAIR_FILE):
        return None
    with open(CURRENT_PAIR_FILE, 'r') as f:
        return f.readline().strip()


def print_current_pair():
    pair = get_current_pair()
    if pair:
        print 'Currently paired with {}'.format(pair)
    else:
        print 'Not currently paired'


def main():
    parser = OptionParser()
    parser.add_option('-l', '--list', dest='list', default=False,
        action='store_true', help='List available pairs')
    parser.add_option('-c', '--current', dest='current', default=False,
        action='store_true', help='Print current pair')
    parser.add_option('-a', '--add', dest='add', default=False,
        action='store_true', help='Add available pair')
    parser.add_option('-r', '--remove', dest='remove', default=False,
        action='store_true', help='Remove pair')
    parser.add_option('-u', '--unpair', dest='unpair', default=False,
        action='store_true', help='Unset current pair')
    (option, args) = parser.parse_args()

    if option.list:
        print_available_pairs()
    elif option.add:
        add_new_pair()
    elif option.remove:
        remove_pair(args[0])
    elif option.unpair:
        unset_pair()
    elif args:
        set_current_pair(args[0])
    else:
        print_current_pair()
