# erors are 2 types
# 1. syntax error
# 2. Runtime errors - Exceptions

try:
    fo=open('himan.txt')
    print(fo.read())
    fo.close()

except:
    print("File not found")
