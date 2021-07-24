

# command-line parsing module in the python standard library 
import argparse
parser = argparse.ArgumentParser()

# adding positional argument 
parser.add_argument("input",type = int,  help = "display a square ") 

# adding verbosity (optional -keyword)
# we can add multiple verbosity by giving type = int and conditioning 
### parser.add_argument("-v", "--verbosity", action = "store_true", help = "increase output verbosity") 

# parser.add_argument("-v", "--verbosity",type = int, choices = [0,1,2], help = "increse the output information")

parser.add_argument("-v", "--verbosity", action = "count", default = 0,  help = "increases the verbosity") 

# getting all the arguments 
args = parser.parse_args() 

def output():
    if args.verbosity >= 2:
        print(f'running {__file__}') 
        print(f"The square of {args.input} is {args.input**2}") 
    elif args.verbosity ==1:
        print(f"The output is {args.input**2}")  
    else :
        print(args.input**2)    

if __name__ == "__main__":
    output()
    print(args)
    




