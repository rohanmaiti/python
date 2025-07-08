"""
The pass Statement
function definitions cannot be empty, but if you for some reason 
have a function definition with no content, put in the pass statement 
to avoid getting an error.
"""

def myfunction():
  pass



#* Function return None if not return statement is there 
def goodDay():
  print('Good day function')

val = goodDay()
print(val)

#* if function is not returning anything then it will return None | similar to js (undefined)
