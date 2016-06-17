from datetime import datetime

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import logging
logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)

# returns raw calendar data
def get_contributions_for_user(username):
  content = requests.get("https://github.com/users/%s/contributions" % username).text

  lines = content.splitlines()
  lines = [x.strip() for x in lines]
  lines = [x for x in lines if x.startswith('<rect class="day"')]

  return lines

# returns YYYY-MMMM-DD strings for each day with a contribution
def get_contribution_days_for_user(username):
  data = get_contributions_for_user(username)
  data = [x[-13:-3] for x in data if "#eeeeee" not in x]
  return data

def get_streak_for_user(username):
  data = get_contributions_for_user(username)

  contribs = []
  offset = len("data-count=")
  for line in data:
    idx = line.find("data-count=") + offset + 1
    line = line[idx:]
    parts = line.split('"')
    count = int(parts[0])
    date = datetime.strptime(parts[2], "%Y-%m-%d")
    contribs.append((count, date))

  if not contribs:
    return 'error'

  # remove dates in the future
  cur = contribs.pop()
  while cur[1] >= datetime.today():
    cur = contribs.pop()  

  if not contribs:
      return 'error'

  # count current streak
  streak = 0
  while cur[0] != 0:
    streak += 1
    cur = contribs.pop()

  return streak

if __name__ == '__main__':
  print get_streak_for_user("csu")