#!/usr/bin/python
import sys

import ghstreak

def main():
  if len(sys.argv) != 2:
    print 'Invalid number of arguments. Usage: ghstreak [username].'
    return

  print ghstreak.get_streak_for_user(sys.argv[1])

if __name__ == '__main__':
  main()