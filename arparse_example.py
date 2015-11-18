import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action='store_true', help="debug output")
parser.add_argument("-n", "--dryrun", action='store_true', help="dry run")
parser.add_argument("dbname", help="db name")
parser.add_argument("dbhost", help="db hostname")
parser.add_argument("dbpasswdfile", help="db password file")
parser.add_argument("filename", help="csv file")
args = parser.parse_args()

print vars(args)
#set logging level using args.debug
dryrun=args.dryrun

