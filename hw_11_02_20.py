# https://www.codewars.com/kata/will-you-make-it

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return( True if distance_to_pump <= mpg * fuel_left else False)


# https://www.codewars.com/kata/will-there-be-enough-space/train/python

def enough(cap, on, wait):
    return( 0 if (on + wait) <= cap else (on + wait - cap));


#https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def areYouPlayingBanjo(name):
    return((name + " plays banjo") if name[0].lower() == 
       "r" else  (name + " does not play banjo"));

#https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python

def bool_to_word(boolean):
   return ('Yes' if boolean else 'No')

#https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
def count_sheeps(sheep):
   return(sheep.count(True))

#https://www.codewars.com/kata/is-this-my-tail/train/python
def correct_tail(body, tail):
     return tail == body[-1]