import time;
def maincountdown(num, usesleep=False):
    if (num == None): raise Exception("num must be an integer, but it was not defined!");
    elif (type(num) == int): pass;
    else: raise Exception("num must be an integer, but it was not defined!");
    while (num > 0):
        print(f"{num} SECOND(S)!");
        if (usesleep): time.sleep(1);
        else: pass;
        num -= 1;
    print("HAPPY NEW YEAR!");
    return None;

def countdown(num):
    return maincountdown(num);

def countdown_with_sleep(num):
    return maincountdown(num, True);

#countdown_with_sleep(10);
