# Jenkins Utilities

This project is a set of utilities for Jenkins.

## Query Jobs

The query jobs script can be used to query jobs by status. The script includes
a help option.

```
$ python query_jobs.py --help
usage: query_jobs.py [-h] [--show-failed] [--show-success] [--show-disabled]
                     [--show-all]
                     hostname

Queries Jenkins jobs.

positional arguments:
  hostname         hostname to check

optional arguments:
  -h, --help       show this help message and exit
  --show-failed    show failed jobs
  --show-success   show successful jobs
  --show-disabled  show disabled jobs
  --show-all       show all jobs
```

For example, to get the failed jobs:

```
$ python3 query_jobs.py <hostname> --show-failed
```
