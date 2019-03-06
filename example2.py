def spam():
    #sets local variable eggs to 99
    eggs = 99
    #a second local scope is created, and in that scope ham is set to 101, eggs to 0
    #when bacon returns, the local scope for that cal is destroyed
    #however, spam() still exists and eggs is set to 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    #another local scope has eggs set to 0
    eggs = 0

#calls function spam, creates local scope
spam()
