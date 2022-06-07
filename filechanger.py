import random
import time

def wait_for_read():
    flag = True
    while(flag):
        time.sleep(0.01)
        f = open("input.hex", "r")
        containings = f.readlines()

        for line in containings:
            if(len(line) == 2):
                if(line[0] == '0'):
                    flag = False

        f.close()

def read():
    output = ""
    time.sleep(0.001)
    f = open("input.hex", "r")
    containings = f.readlines()

    for line in containings:
        if(len(line) == 2):
            output = output + line

    f.close()

    return output

reading = False
buffer = []
while(True):
    if(not reading):
        print("sending")
        usrinpt = input("you: ")
        usrinpt = usrinpt.encode('utf-8')

        for i in range(len(usrinpt)):
            print("putting in pipe: ", int(usrinpt[i]))
            string = ""
            string = "1\n"
            f = open("input.hex", "w")
            
            charidx = 0
            for char in bin(usrinpt[i])[2:]:
                string = string + char + "\n"
                charidx += 1

            for _ in range(charidx, 8):
                string = string + char + "\n"

            f.write(string)
            f.close()
            wait_for_read()    

        print("putting EOF")
        f = open("input.hex", "w")
        f.write("1\n0\n0\n0\n0\n0\n0\n0\n0\n")
        f.close()
        reading = True
        buffer = []
        wait_for_read()

    else:
        wait_for_read()

        r = read()
        r = r.split("\n")

        number = 0
        flag = True
        for i in range(1, 9):
            if i == 0:
                continue

            if r[i] == "1":
                number += 2 ** (7-i)
                flag = False
        
        number = int(number)
        buffer.append(str(number.to_bytes(1, 'big'), 'utf-8'))
        if flag:
            reading = False;
            print("har: ", "".join(buffer))
        else:
            f = open("input.hex", "w")
            f.write("1\n0\n0\n0\n0\n0\n0\n0\n0\n")
            f.close()
