from datetime import datetime
import os
import pathlib
import re
import subprocess
import sys
from urllib.parse import quote

import frontmatter
# import mistletoe
from unidecode import unidecode

def format_article(name):
  with open(name) as f:
    post = frontmatter.load(f)

  # print(post)
  # print(post['title'])

  mddate = post.get("date")
  if not mddate:
    datestr = datetime.today().strftime('%Y-%m-%d')
  else:
    datestr = mddate.strftime('%Y-%m-%d')



  new_name = post['title'].lower()
  new_name = unidecode(new_name)
  new_name = re.sub(r"[ ?]+", "-", f'{datestr}-{new_name}.md')
  new_name = os.path.join(*name.split('/')[:-1], new_name)


  return new_name

def main():
  # path = '_drafts/'
  # article_names = os.walk(path, topdown=True, followlinks=True)
  # images = os.walk('_drafts/assets/writing', topdown=True, followlinks=True )

  imagesobj = pathlib.Path('_posts')

  renames = {}
  images = imagesobj.rglob('*')
  for ximage in images:
    image = str(ximage)
    if "/_draft" in image: continue
    if not (" " in image and "assets" in image and os.path.isfile(image)):
      continue

    new_name = unidecode(image.replace(" ", "-")).lower()
    new_name = re.sub(r"[,'?]*", "", new_name)
    renames[image] = new_name

  for old_path, new_path in renames.items():
    old_name = old_path.split('/')[-1]
    old_name_encoded = quote(old_name.split('/')[-1])
    for oname in imagesobj.rglob('*.md'):
      parts = str(oname).split('/')
      fname = parts[-1]
      # if str(fname)[-3:] != '.md': continue
      # if " " in str(fname): continue
      content = open(oname, 'r').read()
      if old_name_encoded not in content:
        continue
      print(f'{old_name} -> {old_name_encoded}')
      with open(str(oname), 'w') as f:
        new_name = new_path.split('/')[-1]
        content = (content
            .replace(old_name_encoded, new_name)
            .replace(f'assets/writing/', 'https://siran.github.io/assets/writing/'))

        f.write(content)
      os.rename(image, new_name)
      print(f"renamed: {image} -> {image.replace(' ', '-')}")

      written = 1

  article_pathnames = imagesobj.glob('*.md')
  for ppath in article_pathnames:
    path = str(ppath)
    fname = path.split('/')[-1]
    if fname[4] == '-' and fname[7] == '-': continue
    if not os.path.isfile(path): continue
    if fname[0] == '.': continue
    if "_draft" in path: continue


    # if (fname[4] != '-' and fname[7] != '-'):

    # apparently to date only one article
    # if sys.argv[1] not in fname: continue

    print(fname)
    new_path = format_article(path)
    os.rename(path, new_path)
    print(f"renombrado: {new_path} <- {fname}")

if __name__ == '__main__':
  main()
