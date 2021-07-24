import argparse
parser = argparse.ArgumentParser(description="process some integers", usage = "provide list of numbers", epilog=None)
parser.add_argument('integers', metavar = 'N', type = int, nargs="+", help = "an integer for the accumulator")
parser.add_argument('--sum', dest = 'accumulate', action = 'store_const', const = sum, default = max, help = "sum the integers(default= max)")


# parse_args() will return an object with two attributes integers and accumulate. 
# accumulate attribute will be either the sum() or max() 
args = parser.parse_args() 

if __name__ == '__main__':
    print(args.accumulate(args.integers))
    print(parser.prog)
    print(parser.usage)
    print(parser.description) 

