from datetime import datetime
import os
import re

import frontmatter
import mistletoe
from unidecode import unidecode

os.chdir('/d/Users/an/Documents/__dev/writing/_posts')

def format_article(name):
  with open(name) as f:
    post = frontmatter.load(f)

  with open(name) as fin:
    rendered = mistletoe.Document(fin)
  # print(post)
  # print(post['title'])


  mddate = post.get("date")
  if not mddate:
    datestr = datetime.today().strftime('%Y-%m-%d')
  else:
    datestr = mddate.strftime('%Y-%m-%d')

  new_name = post['title'].lower()
  new_name = unidecode(new_name)
  new_name = re.sub(r"[ ]+", "-", f'{datestr}-{new_name}.md')

  os.rename(name, new_name)
  return new_name

def main():
  article_names = os.listdir()

  for name in article_names:
    if name[-3:] != '.md': continue

    if (not os.path.isfile(name)
        or name[0] == '.'): continue

    print(name)
    if (name[4] != '-' and name[7] != '-'):
      new_name = format_article(name)
      print(f"formatted: {new_name} <- {name}")

if __name__ == '__main__':
  main()
