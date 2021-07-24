import argparse
parser = argparse.ArgumentParser(
    prog = 'PROGRAM',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--foo', type = int, default = 32, help = 'help of foo arg')
parser.add_argument('bar', nargs = "*", default = [1,2,3], help  = 'help of bar')

parser.print_help()

