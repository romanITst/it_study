#!/usr/bin/env python3

import sys

def dictify_logline(line):
  '''
  returns a dictionary containing information extracted from
  a combined log file.
  Currently, we are only interested in the addresses of remote hosts
  and the amount of transmitted bytes, but for a complete picture, we
  have added a selection of status code.
  '''

  split_line = line.split()
  return {'remote_host' : split_line[0],
          'status': split_line[8],
          'bytes_sent': split_line[9],
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
    # print(line_dict)
    try:
      bytes_sent = int(line_dict['bytes_sent'])
    except ValueError:
    # ignore errors
      continue
    report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_sent)
  return report_dict

if __name__ == "__main__":
  if not len(sys.argv) > 1:
    sys.exit(1)
  infile_name = sys.argv[1]
  try:
    with open(infile_name, 'r') as log:
      log_report = generate_log_report(log)
      print(log_report)
  except IOError:
    print("You must specify a valid file to parse")
    sys.exit(1)