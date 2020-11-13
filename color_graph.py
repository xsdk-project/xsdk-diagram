#!/usr/bin/python3

import re
import sys

packages=[
"alquimia",
"amrex",
"butterflypack",
"datatransferkit",
"dealii",
"ginkgo",
"heffte",
"hypre",
"magma",
"mfem",
"netlib-scalapack",
"omega-h",
"petsc",
"pflotran",
"phist",
"plasma",
"precice",
"pumi",
"py-libensemble",
"slate",
"slepc",
"strumpack",
"sundials",
"superlu-dist",
"tasmanian",
"trilinos"
]

p = re.compile('\[label="[^"]+"\]')
with open(sys.argv[1]) as fp:
  for line in fp:
    match = None
    xsdk = False
    for pkg in packages:
      if pkg in line:
        match = pkg
        break
      if 'xsdk' in line:
        xsdk = True
        break
    if match:
      print(p.sub('[label="%s", fillcolor=chartreuse4]' % match, line), end='')
    if xsdk:
      print(p.sub('[label="xsdk", fillcolor=brown]', line), end='')
    else:
      print(line, end='')
