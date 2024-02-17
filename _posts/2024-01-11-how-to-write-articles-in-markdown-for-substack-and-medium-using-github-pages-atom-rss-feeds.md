---
title: How to write articles in Markdown for Substack and Medium using GitHub Page's Atom/RSS feed
excerpt: You can write all your articles using Markdown and get them to Substack using Jekyll's jekyll-feed's plugin's Atom (RSS-like) feed to import articles into Substack.
canonical_url: https://anrodriguez.substack.com/p/how-to-write-articles-in-markdown-for-substack-and-medium-using-github-pages-atom-rss-feedshtml
tags:
  - devops
  - technical
---
It is possible (and not hard) to have all your beautiful articles in plain-text format, backed-up and versioned-controlled.

If you write online you might find this useful.

You can write all your articles using [Markdown](https://en.wikipedia.org/wiki/Markdown) and then import them to Substack using [Jekyll](https://jekyllrb.com/)'s [jekyll-feed](https://github.com/jekyll/jekyll-feed) plugin's Atom (RSS-like) feed to import articles into Substack.

All your articles in plain-text format, backed-up and versioned-controlled.

## Canonical URL remains in Substack
Substack always retains the canonical URL. When Medium or Dev.to import articles, they respect Substack's canonical URL.

## My articles in Markdown
I like the idea of having my articles written down in markdown and version controlled with Git.

It makes it easy to post code
```python
def myfunc():
   pass
```

Probably even some Latex $E=mc^2$. If not now, I might be able to make it work in the future.

In my local editor it looks OK:

![](https://siran.github.io/assets/writing/test-image.png)

*[Testing a caption for the image](https://siran.github.io/assets/writing/test-image.png)*

## Setting it up
It was not so hard to set up GitHub pages. I followed [this tutorial](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll) among other many tutorials. 

ChatGPT help me to resolve Rube installation problems.

I do have some computing skills (I already knew Git, Markdown, etc.), so that helped. 

## Tests and improvements
I am still testing if the Jekyll->Github Pages->RSS->Substack pipeline is the right solution. I still don't know if platforms will behave as expected over time. The good thing is that my articles are safe in markdown format in my computer and cloud backups, and available as well in a [Github Page](https://siran.github.io/writing/).

It's also easy to run the static page locally.
## If development stops means there are no more developers
Development never stops.

Next I plan to implement [Staticman](https://staticman.net/), to allow for version-controlled comments for my articles.

Also it looks appealing to write a simple script to automate the article timestamping. Also, probably, another script to automate the canonical URL update for the articles posted in Github.


---


So this is all the pipeline test for now.

Comment, like and subscribe. :-)

(update: pipeline seems to work fine. Updated canonical URL in the GitHub page to point to Substack. Substack is like my main publisher; Github is the preprint; Medium and Dev.to the communicators.)
