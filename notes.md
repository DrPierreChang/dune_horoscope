The most common way to print colored text to the terminal
is by printing ANSI escape sequences.
For a simple example,
here's some Python code from the Blender build scripts:

~~~~python
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# To use code like this, you can do something like:
print(f"{Bcolors.WARNING}Warning: No active frommets remain. Continue?{Bcolors.ENDC}")
~~~~





