#!/usr/bin/env python3


# Description: Logs parser script   ....    ....    ....    ..... 


import sys
import re

log_line_re = re.compile(r'''(?P<remote_host>\S+) #ip ADDRESS
                              \s+ #whitespace
                              \S+ #remote logname
                              \s+ #whitespace
                              \S+ #remote user
                              \s+ #whitespace
                              \[(?P<Time>.*) \+\d{4}\] #time
                              \s+ #whitespace
                              "[^"]+" #first line of request
                              \s+ #whitespace
                              (?P<status>\d+)
                              \s+ #whitespace
                              (?P<bytes_sent>-|\d+)
                              \s* #whitespace
                              "-"\s+# "-" + whitespace
                              "(?P<agent>.*)"
                              ''', re.VERBOSE)

def dictify_logline(line):
  '''
  returns a dictionary containing information extracted from
  a combined log file.
  Currently, we are only interested in the addresses of remote hosts
  and the amount of transmitted bytes, but for a complete picture, we
  have added a selection of status code.
  '''
  m = log_line_re.match(line)
  if m:
    groupdict = m.groupdict()
    if groupdict['bytes_sent'] == '-':
      groupdict['bytes_sent'] = '0'
    return groupdict
  else:
    return {'remote_host': None,
    'status': None,
    'bytes_sent': "0",
    'agent': "-"
    }

def generate_log_report(logfile):
  '''
  returns a dictionary in the format:
  remote_host => [list of transmitted byte counts]
  This function takes a file object, traverses all the lines
  in the file, and creates a report on the number of bytes transmitted
  during each request from a remote host to the web server.
  '''
  report_dict = {}
  for line in logfile:
    line_dict = dictify_logline(line)
    try:
      bytes_sent = int(line_dict['bytes_sent'])
    except ValueError:
    # ignore all errors
      continue
    report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_sent)
  return report_dict

def get_sum_of_bytes(logfile):
  sumofb = []
  for line in logfile:
    line_dict = dictify_logline(line)
    bytes_sent = line_dict['bytes_sent']
    sumofb.append(bytes_sent)
    sumofb1 = sumofb.append(bytes_sent)
    return sumofb1
  sumofb1
  return sumofb1
  # return {
    # "ip_address": "sum_of_bytes"
  # }

if __name__ == "__main__":
  if not len(sys.argv) > 1:
    print(__doc__)
    sys.exit(1)
  infile_name = sys.argv[1]
  try:
    with open(infile_name, 'r') as log:
      log_report = generate_log_report(log)
      sumofb2 = get_sum_of_bytes(log)
    print(log_report)
    print(sumofb2)
  except IOError:
    print("You must specify a valid file to parse")
    print(__doc__)
    sys.exit(1)