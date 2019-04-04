#yippie.py
from __future__ import print_function, unicode_literals
import os, sys
import copy, re #ruh roh

if sys.argv[-1][-4:] == ".yip":
	code = open(sys.argv[-1]).read()
	code = "".join(re.split("\n|\t", code))
else:
	print("No .yip file")
	quit()

CLASSES = {"main": {"code":[], "data":{}}}

while code[:6] == "CLASS ":
	code = code[6:]
	name = code[:code.index(" ")]
	code = code[code.index("{")+1:]
	CLASSES[name] = {"code":code[:code.index("}")], "data":{}}
	code = code[code.index("}")+1:]

NODES = [CLASSES["main"]]

def advance(node):
	code, data = node['code'], node['data']
	cmd = code[:code.index(";")]
	if cmd.startswith("make "):
		cmd = cmd[5:]
		clas = cmd[:cmd.index(" ")]
		name = cmd[len(name)+1:]
		data[name] = copy.deepcopy(CLASSES[clas])
		NODES.append(data[name])

	elif cmd.startswith("goto "):
		cmd = cmd[5:]
		l = len(cmd)
		node['code'] = code[code.index("flag " + cmd) + 5 + l:] + code[:code.index("flag " + cmd) - 5 - l]

	elif cmd == "END":
		NODES.remove(node)

	code = code[len(cmd):] + cmd + ";"

while NODES:
	for node in NODES:
		advance(node)
