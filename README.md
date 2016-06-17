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
# In the api directory
pip install -r requirements.txt
python server.py
```
