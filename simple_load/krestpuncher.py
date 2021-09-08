from subprocess import Popen, PIPE

class KrestPuncher(object):
    def __init__(self, host, count, rate, locust_file, log_file, duration=None):
        self.host = f"http://{host}/api/v0"
        self.count = count
        self.rate = rate
        self.duration = duration
        self.locust_file = locust_file
        self.log_file = log_file

    def generate_locust_file(self):
        # create a file
        # take parameters
        # add or pass them into the locust file
        pass


    def start_load(self):
        # use subprocess to call locust
        global proc
        with open(self.log_file, 'w') as fp:
            proc = Popen(['locust', '--no-web', '-c', self.count,
                        '-r', self.rate, #'-t', self.duration,
                        '-H', self.host, '-f', self.locust_file,
                        ], stdout=fp, stderr=fp)

    def stop_load(self):
        # end the load test by sending a SIGTERM
        proc.kill()
