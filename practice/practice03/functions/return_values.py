def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


def myfunc():
  global x
  x = 300

myfunc()

print(x)