import ssl
import json
import argparse
from urllib.request import urlopen
from colorama import init, Fore

python_api_url = 'https://{}/jenkins/api/json'

def get_cert():
    cert = ssl.create_default_context();
    cert.check_hostname=False
    cert.verify_mode=ssl.CERT_NONE
    return cert

def get_json(hostname):
    cert = get_cert()
    url = python_api_url.format(hostname)
    with urlopen(url, context = cert) as response:
       return json.load(response)

def output_job(job, show_success, show_failed, show_disabled, show_all):
    name = job['name']
    color = job['color']
    if color == 'blue' and (show_success or show_all):
        print(Fore.GREEN + name)
    if color == 'red' and (show_failed or show_all):
        print(Fore.RED + name)
    if color == 'disabled' and (show_disabled or show_all):
        print(Fore.MAGENTA + name)

def output_jobs(hostname, show_success, show_failed, show_disabled, show_all):
    result = get_json(hostname)
    for job in result['jobs']:
        output_job(job, show_success, show_failed, show_disabled, show_all)

def parse_args():
    parser = argparse.ArgumentParser(description='Queries Jenkins jobs.')
    parser.add_argument('hostname', help='hostname to check'),
    parser.add_argument('--show-failed', help='show failed jobs',
                        action='store_true')
    parser.add_argument('--show-success', help='show successful jobs',
                        action='store_true')
    parser.add_argument('--show-disabled', help='show disabled jobs',
                        action='store_true')
    parser.add_argument('--show-all', help='show all jobs',
                        action='store_true')
    return parser.parse_args()

def main():
    init()

    args = parse_args()
    hostname = args.hostname
    show_success = args.show_success
    show_failed = args.show_failed
    show_disabled = args.show_disabled
    show_all = args.show_all

    output_jobs(hostname, show_success, show_failed, show_disabled, show_all)

if __name__ == '__main__':
    main()
