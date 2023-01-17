import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_error(*args, **kwargs):
    """print the defines message to stderr and then exit(84)
    """
    print(bcolors.FAIL + "ERROR:\t" + bcolors.ENDC + "".join(map(str,args)), file=sys.stderr, **kwargs)
    sys.exit(84)