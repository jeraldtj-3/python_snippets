
import argparse

parser = argparse.ArgumentParser(description = "calculating the power of x to the power of y")  
parser.add_argument("-x", "--input_x", type = int, help = "base value") 
parser.add_argument("-y", "--input_y", type = int, help = "exponent")

# groups
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action = "store_true") 
group.add_argument("-q", "--quiet", action = "store_true") 

args = parser.parse_args()
answer = args.input_x ** args.input_y
def main():
    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.input_x} to the power {args.input_y} is {answer}.") 
    else :
        print(f"{args.input_x}^{args.input_y} = {answer}") 

if __name__ == '__main__':
    main()
    
# Note : [-v|-q] tells that we can either use one not both at the same time.





