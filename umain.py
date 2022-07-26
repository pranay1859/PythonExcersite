def do_stuff(arg):
    try:
        if arg:
            return arg+5
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err