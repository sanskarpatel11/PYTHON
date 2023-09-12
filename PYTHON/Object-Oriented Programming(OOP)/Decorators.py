def gm(fuc):
  def mx(*args, **kwargs):
    print("Good Morning")
    fuc(*args, **kwargs)
    print("Thanks for using this function")
  return mx

@gm
def hell():
  print("Hello world")

@gm
def add(a, b):
  print((a+b)/2)
  
# greet(hello)()
hell()
# greet(add)(1, 2)
add(1, 2)