import time

for i in range(10):
    print('FOR Iteration number ' + str(i))
    time.sleep(1)

    j = 1
    while j != 10:
        if (j == 5) or (j == 4 and i != 3) or (j == 3) or (j == 2):
            try:
                print('WHILE Iteration number ' +str(k))
            except Exception as e:
                print('HEY ! EXCEPTION: ' + str(e))
                result = i + j
                print('Result: ' + str(result))
        elif j == 4 and i == 3:
            print('HEY! J is ' + str(j) + ' and I is ' + str(i))
        else:
            print('Not checked')
        j += 1
        time.sleep(0.5)