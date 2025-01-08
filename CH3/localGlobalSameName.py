def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local' #prints 'bacon local'
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs) #printsj 'global'