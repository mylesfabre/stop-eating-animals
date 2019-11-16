# Myles Fabre
# hw8pr3.py
# 20 Questions
# (question, yes, no)

tree =("Is it bigger than a breadbox?",("Is it an elephant?"),("Is it a mouse?"))
def play(tree):
    first = input(tree[0])
    if first in ['y', 'Y', 'yes', 'YES', 'Yes', 'yEs', 'yES', 'yeS']:
        second = input(tree[1])
        if second in ['y', 'Y', 'yes', 'YES', 'Yes', 'yEs', 'yES', 'yeS']:
            print("I got it!")
        else:
            alternate = input("DARN! What was it?")
            reason = input("What distinguisishes "+alternate+" from "+tree[1]+"?")
            tree[1].append(reason)
    else:
        alternate = input("DARN! What was it?")
        reason = input("What distinguisishes "+alternate+" from "+tree[2]+"?")
        tree[2].append(reason)
    return tree