# gh-streak

A Python library, CLI, and API for fetching GitHub contribution streaks.

## Installation
```bash
pip install ghstreak
```

## Usage
### CLI
```bash
# Get the current streak for csu
ghstreak csu
```

### Python Library
```python
import ghstreak

# Get the current streak for csu
ghstreak.get_streak_for_user('csu')
```

### HTTP API
```bash
git clone git@github.com:csu/gh-streak.git
cd api
pip install -r requirements.txt
python server.py
```

## Contributing
Pull requests and issues are welcome.

### Maintainers
* [Christopher Su](https://christopher.su) ([@csu](https://github.com/csu))
