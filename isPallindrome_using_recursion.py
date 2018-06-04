def isPal(string):
    str2list = list(string)
    if len(str2list) == 0 or len(str2list) == 1:
        return True
    elif str2list[0] == str2list[-1]:
        return isPal(str2list[1: -1])
    else:
        return False


print(isPal("UNIINU"))
