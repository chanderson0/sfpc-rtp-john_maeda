import re
import os

def replacer(infile, replacements, outfile):
  f = open(infile, 'r')
  filedata = f.read()
  f.close()

  newdata = filedata
  for replacement in replacements:
    newdata = newdata.replace(replacement[0], replacement[1])

  os.makedirs(os.path.dirname(outfile), exist_ok=True)
  f = open(outfile, 'w')
  f.write(newdata)
  f.close()

for i in range(100):
  val1 = (i * 4) - 200
  val2 = (i * 8) - 400

  infile = 'morisawa_fun.ps.tpl'
  outfile = "out_ps/morisawa_fun-" + str(i) + ".ps"

  replacements = [['!!VARYME1!!', str(val1)], ['!!VARYME2!!', str(val2)]]
  replacer(infile, replacements, outfile)
