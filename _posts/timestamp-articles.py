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

# os.chdir('/d/Users/an/Documents/__dev/writing/_posts')

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
  images = article_names = imagesobj.rglob('*')

  renames = {}
  # for ximage in imagesobj.rglob('*'):
  #   image = str(ximage)
  #   if " " in image and "assets" in image:
  #     old_name = image
  #     new_name = unidecode(image.replace(" ", "-")).lower()
  #     new_name = re.sub(r"[,]", "", new_name)
  #     os.rename(image, new_name)
  #     renames[image] = new_name
  #     print(f"renamed: {image} -> {image.replace(' ', '-')}")

  renames = {'_posts/assets/writing/I write to find out what I am thinking - Joan Didion.png': '_posts/assets/writing/i-write-to-find-out-what-i-am-thinking---joan-didion.png', '_posts/assets/writing/I write to find out what I think - Stephen King.png': '_posts/assets/writing/i-write-to-find-out-what-i-think---stephen-king.png'}

  for old_path, new_path in renames.items():
    old_name = old_path.split('/')[-1]
    old_name_encoded = quote(old_name.split('/')[-1])
    for oname in imagesobj.rglob('*'):
      parts = str(oname).split('/')
      fname = parts[-1]
      if " " in str(fname): continue
      if str(fname)[-3:] != '.md': continue
      content = open(oname, 'r').read()
      if old_name_encoded not in content:
        continue
      print(f'{old_name} -> {old_name_encoded}')
      with open(str(oname), 'w') as f:
        new_name = new_path.split('/')[-1]
        content = content.replace(old_name_encoded, new_name)
        f.write(content)
      written = 1

  # for ppath in imagesobj.rglob('*'):
  #   path = str(ppath)
  #   fname = path.split('/')[-1]
  #   print(fname)
  #   if fname[-3:] != '.md': continue

  #   if (not os.path.isfile(path)
  #       or fname[0] == '.'): continue

  #   if (fname[4] != '-' and fname[7] != '-'):
  #     if sys.argv[1] not in fname: continue
  #     new_path = format_article(path)
  #     os.rename(path, new_path)
  #     print(f"formatted draft: {new_path} <- {fname}")

if __name__ == '__main__':
  main()
