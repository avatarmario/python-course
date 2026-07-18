def print_exception_hierarchy(exc, level=0):
    print(" " * level + str(exc))
    for subclass in exc.__subclasses__():
        print_exception_hierarchy(subclass, level + 2)

print_exception_hierarchy(Exception)