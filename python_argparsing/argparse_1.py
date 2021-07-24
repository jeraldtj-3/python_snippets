import argparse

parser = argparse.ArgumentParser(
    prog = "testing program",
    usage = '%(prog)s [options]', 
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = """
        Please read this description for running this program
        =====================================================
        This is a test function , which you can use for text processing.
        arguments and epilog can be found in the following lines.
        Thank you : 
    """,
    epilog = """likewise for this epilog whose whitespace will be cleaned up and whose words ...""")

parser.add_argument('--foo', help = "foo help in the %(prog)s program.") 
parser.add_argument("bar", nargs = '+', help = "bar help") 
args = parser.parse_args()



