pairwith
========

A small utility that aims to give credit to both members of a pair while they work together. 

Usually, when pairing, one member of the pair does all the committing and gets credit for all the work as the author of the commit. This utility adds a `Co-Authored-By` tag with the other pair's name to the commit message so everyone gets proper credit for the work.

Installation
------------

To install the application, clone this repo and run:

```bash
python setup.py install
```

The `Co-Authored-By` tag is added by a Git commit hook, so you'll need to copy the `prepare-commit-msg` file to `.git/hooks/` in every repo you want to use `pairwith` in. Or, you can create a git template containing the commit hook:

```bash
$ mkdir -p ~/.git_template/hooks
$ cp prepare-commit-msg ~/.git_template/hooks
```

Then, you can run `git init` in a repo to have the commit hook copied to that repo (even if it's not a new repo).

Usage
-----

`pairwith` provides options for adding/removing pairs, setting the current pair, and listing available pairs:

```
Usage: pairwith [options]

Options:
  -h, --help     show this help message and exit
  -l, --list     List available pairs
  -c, --current  Print current pair
  -a, --add      Add available pair
  -r, --remove   Remove pair
  -u, --unpair   Unset current pair
```

Example
-------

Use `pairwith -a` to add a new pairing partner and specify a nickname, full name, and email for them:

```
$ pairwith -a
Enter nickname: randy
Enter full name: Randy Butternubs
Enter email: randy@butternubs.me
```

To see the list of available pairs, you can execute:

```
$ pairwith -l
Available pairs:
    randy           Randy Butternubs <randy@butternubs.me>
    starlord        Peter Quill <starlord@guardians.com>
```

When pairing with someone, you can give `pairwith` their nickname:

```
$ pairwith randy
```

Now, the next time you commit, the commit message will already contain your pair's information:

```

Co-Authored-By: Randy Butternubs <randy@butternubs.me>

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Your branch is up-to-date with 'origin/master'.
```

When done pairing, you can remove the current pair infromation using:

```
$ pairwith -u
```
