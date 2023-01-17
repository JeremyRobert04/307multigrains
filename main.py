#!/usr/bin/env python3

import sys

from src.my_parser import MyParser as Parser
from src.simplexe import Simplexe

def main(args=None):
    if args is None:
        args = sys.argv

    parser = Parser(args)
    simplexe = Simplexe(parser.get_parsed_args())
    simplexe.run()
    simplexe.print_result()

    sys.exit(0)

if __name__ == '__main__':
    main()