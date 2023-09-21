def read_int(prompt, min_, max_):
    running = True
    set_ = [x for x in range(min_,max_+1)]
    val = None
    while running:
        try:
            val = int(input(prompt))
            assert val in set_
            break
        except ValueError:
            print('Error: wrong input')
            continue
        except AssertionError:
            print('Error: the value is not within permitted range (min..max)')
            continue
    return val

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
