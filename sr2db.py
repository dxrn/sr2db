import argparse
from qb import *

def main(args):

    if args.c != None:
        DATABASE_NAME = args.c[0]
        YEAR = args.c[1]
        create_db(format_data(YEAR), DATABASE_NAME)
    elif args.d != None:
        DATABASE_NAME = args.d[0]
        monthly_demand(DATABASE_NAME)
    elif args.s != None:
        pass
    else:
        print("No arguments passed") 
        parser.print_help()     
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--c', help='Builds database using Amazon Seller Reports, takes two arguments, DATABASE_NAME &  YEAR.', nargs=2)
    parser.add_argument('--d', help='Builds a csv file containing units ordered per month grouped by Child ASIN, takes argument, DATABASE_NAME.', nargs=1)

    args = parser.parse_args()

    main(args)