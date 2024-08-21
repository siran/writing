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

def replace_text_in_files():
  # The sed command to modify the files
  os.chdir("/d/Users/an/Documents/__dev/writing/_posts")
  command = "sed --in-place -E 's#\(assets/writing/#(https://siran.github.io/assets/writing/#g' *.md"

  # Using subprocess to run both commands together
  result = subprocess.run(
      command,
      text=True,
      shell=True
  )

  # Print the output which includes filenames and changed lines
  print(result.stdout)
  if result.stderr:
      print("Errors:", result.stderr)

def main():
  # path = '_drafts/'
  # article_names = os.walk(path, topdown=True, followlinks=True)
  # images = os.walk('_drafts/assets/writing', topdown=True, followlinks=True )

  # imagesobj = pathlib.Path('_posts')

  renames = {}
  # images = imagesobj.rglob('*')
  # for ximage in images:
  #   image = str(ximage)
  #   if "/_draft" in image: continue
  #   if not (" " in image and "assets" in image and os.path.isfile(image)):
  #     continue

  #   new_name = unidecode(image.replace(" ", "-")).lower()
  #   new_name = re.sub(r"[,'?]*", "", new_name)
  #   renames[image] = new_name

  replace_text_in_files()

  os.chdir("/d/Users/an/Documents/__dev/writing/")
  imagesobj = pathlib.Path('_posts')
  article_pathnames = imagesobj.rglob('*.md')
  for ppath in article_pathnames:
    path = str(ppath)
    fname = path.split('/')[-1]
    if fname[4] == '-' and fname[7] == '-': continue
    if not os.path.isfile(path): continue
    if fname[0] == '.': continue
    if "_draft" in path: continue

    new_path = format_article(path)
    os.rename(path, new_path)
    print(f"renombrado: {new_path} <- {fname}")

if __name__ == '__main__':
  main()
