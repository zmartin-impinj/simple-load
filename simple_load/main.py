import configargparse
from krestpuncher import KrestPuncher

def parse_args():
    p = configargparse.ArgParser()
    p.add('-H', '--reader-hostname', required=True)
    p.add('--rate', required=True)
    p.add('--clients', required=True)
    p.add('--run-time', required=False)

    args = p.parse_args()
    return args

def main():
    args = parse_args()
    if not args.run_time:
        args.add('run_time', None)
    kp = KrestPuncher(args.reader_hostname, args.rate, args.clients, args.run_time)
    print(args)

    kp.run_load()

if __name__ == '__main__':
    main()
