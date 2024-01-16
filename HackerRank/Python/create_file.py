#!/usr/local/bin/python3
#NOTE: This script stubs a challenge file, but it is old. Should consider updating

file_name = input("what is the name of the challenge: ")
f = open(file_name + ".py", "x")
f.write("try:\n    from raw_input import input\nexcept ImportError:\n    pass")
f.close()
