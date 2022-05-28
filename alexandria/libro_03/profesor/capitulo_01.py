#!/usr/bin/python3
# usage: ./capitulo_01.py
# Evaluador libro_03 capitulo_01

import base64
import codecs


flag = "pzyhrJuhpJWyYzAfXvZdAaRjBQx1AQt0AT4jpwOjA243pGp3BQH3ZQMjAGLlAwDdVlblXvZdpayjoz1hXvZdMfBuolNlBPO6ozjtZwNlZvNkAQbjAGblAvODHHpX"

flag = codecs.encode(flag, "rot_13")
flag = base64.b64decode(flag).strip()
flag = flag.decode("utf-8")
flag = codecs.encode(flag, "rot_13")

print(flag)

flag = flag.split("*#*")

print(flag)