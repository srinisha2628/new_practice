atup_1 = ('I', 'am', 'a', 'test', 'tuple')
def oddtuples(atup_1):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    sum = ()
    for i in range(0, len(atup_1) + 1, 2):
        sum += (atup_1[i],)
    print(sum)

oddtuples(atup_1)