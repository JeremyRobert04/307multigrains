import sys
import src.my_print as Print

# USAGE
#   ./307multigrains n1 n2 n3 n4 po pw pc pb ps
# DESCRIPTION
#   n1 number of tons of fertilizer F1
#   n2 number of tons of fertilizer F2
#   n3 number of tons of fertilizer F3
#   n4 number of tons of fertilizer F4
#   po price of one unit of oat
#   pw price of one unit of wheat
#   pc price of one unit of corn
#   pb price of one unit of barley
#   ps price of one unit of soy

def safeIntConverter(number: str) -> int | None:
        """Safely convert a string to it corresponding number

        Args:
            number (str): string representing the number

        Returns:
            int | None: the number (int) or None if failed
        """
        try:
            result = int(number)
            return result
        except:
            return None

def print_help() -> None:
    """display Help to start the programs

    Returns:
        None: No return
    """

    print("USAGE")
    print("\t./307multigrains n1 n2 n3 n4 po pw pc pb ps\n")
    print("DESCRIPTION")
    print("\tn1\t\tnumber of tons of fertilizer F1")
    print("\tn2\t\tnumber of tons of fertilizer F2")
    print("\tn3\t\tnumber of tons of fertilizer F3")
    print("\tn4\t\tnumber of tons of fertilizer F4")
    print("\tpo\t\tprice of one unit of oat")
    print("\tpw\t\tprice of one unit of wheat")
    print("\tpc\t\tprice of one unit of corn")
    print("\tpb\t\tprice of one unit of barley")
    print("\tps\t\tprice of one unit of soy")
    sys.exit(0)


class MyParser():
    def __init__(self, args = []) -> None:
        self.args = [x for ind, x in enumerate(args) if ind != 0]
        self.parsed_args = []
        self.parsed_dict = {
            'n1': None,
            'n2': None,
            'n3': None,
            'n4': None,
            'po': None,
            'pw': None,
            'pc': None,
            'pb': None,
            'ps': None
        }
        self.check_cmd()

    def get_parsed_args(self) -> dict:
        """get the parsed args from class

        Returns:
            dict: dictionnary of parsed input
        """
        for arg, index in zip(self.parsed_dict, range(0, len(self.parsed_args))):
            self.parsed_dict[arg] = self.parsed_args[index]
        return self.parsed_dict

    def get_non_parsed_args(self) -> list:
        """get the non parsed args from class

        Returns:
            list: sys.argv without first arguments (./307multigrains)
        """
        return self.args

    def check_for_help(self) -> None:
        """check if -h or --help do display help
        """
        if self.args[0] in ("-h", "--help"):
            print_help()

    def check_cmd(self):
        if not self.args:
            Print.print_error("Missing parameters\n\tDo -h the see help.")
        self.check_for_help()
        if len(self.args) < 9:
            Print.print_error(f"Not enough arguments. Got {len(self.args)} but expected 9")
        if len(self.args) > 9:
            Print.print_error(f"Too many arguments. Got {len(self.args)} but expected 9")
        self.parsed_args = [ safeIntConverter(value) for value in self.args]
        if any(value is None for value in self.parsed_args):
            Print.print_error("Parameters should only contains positive numbers.")
        if not all(i >= 0 for i in self.parsed_args):
            Print.print_error("Parameters should only contains positive numbers.")
