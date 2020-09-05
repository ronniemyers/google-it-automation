import re
log = "July 31 07:51:48 mycomputer bad process[12345]: ERROR Performing package upgrade"

def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  if result is None:
    return ""
  return result[1]

print(extract_pid(log))