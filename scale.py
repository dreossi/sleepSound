# Generate a major scale
def getMajScale(root):
    second = root+2     #w
    third = second+2    #w
    fourth = third+1    #h
    fifth = fourth+2    #w
    sixth = fifth+2     #w
    seventh = sixth+2    #w
    eigth = seventh+1    #h
    
    scale = [root, second, third, fourth, fifth, sixth, seventh, eigth]
    return scale

# Generate a minor scale
def getMinScale(root):
    second = root+2     #w
    third = second+1    #h
    fourth = third+2    #w
    fifth = fourth+2    #w
    sixth = fifth+1     #h
    seventh = sixth+2    #w
    eigth = seventh+2    #w
    
    scale = [root, second, third, fourth, fifth, sixth, seventh, eigth]
    return scale