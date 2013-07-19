import nytimes
import time

i = 1
user = str(raw_input("Username: "))
passwd = str(raw_input("PW: "))
upload = True	

while 1:

    nytimes.main(user, passwd, upload)
    print i
    i += 1
    time.sleep(600)

