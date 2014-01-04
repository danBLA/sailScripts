def run(command):
   try:
      import subprocess as sp
      returnvalue = sp.call(command)
   except ImportError:
      import os
      returnvalue = os.WEXITSTATUS(os.system(" ".join(command)))

   return returnvalue
