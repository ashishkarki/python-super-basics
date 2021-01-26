import modules

modules.clearer()


def foo(name):
    print("foo() is printing: '", name, "' from arguments.", sep='')
    print('this is just another line to show indentation')
    modules.printer('example of using fx from another module')


foo("Ashish")
