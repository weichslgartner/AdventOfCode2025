from requests import get
from pathlib import Path
from markdownify import markdownify as md

year=2025

cookie = open(".cookie", 'r').readline().strip()
cookies = {'session': cookie}
for day in range(1,26):
    raw_input = get(f"https://adventofcode.com/{year}/day/{day}", cookies=cookies)
    Path(f"tasks/{day:02d}.md").open("w").write(md(raw_input.content))
