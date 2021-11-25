class A:

  def __init__(self,string):

   [print(chr(219-ord(c))if'`'<c<'{'else c,end='')for c in string.lower()]
