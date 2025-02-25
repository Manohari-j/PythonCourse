# to breakup large program into reusable sep files. import buil in / own modules
# math

# variable scope:where a var is visible and accessible
# scope Resolution: LEGB local, enclosed, global, built-in

# if__name__ == __main__: this script can be imported or run standalone
# func and classes in this module can be reused without the main block of code executing
# EX:library : Import lib for functionality
def main():
    pass

# modular, readable, avoid unintended execution
if __name__ == '__main__':
    main()