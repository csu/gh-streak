import requests

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
  data = get_contribution_days_for_user(username)

if __name__ == '__main__':
  get_contribution_days_for_user("csu")