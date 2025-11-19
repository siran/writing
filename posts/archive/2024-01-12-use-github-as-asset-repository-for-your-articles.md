---
title: Use GitHub as asset repository for your articles (a.k.a. linking images to GitHub)
excerpt: Imgur doesn't allow hot-linking images, so I switched to GitHubb as my asset repository.
canonical_url: https://anrodriguez.substack.com/p/use-github-as-asset-repository-for-your-articles-aka-hot-linking-images-to-githubhtml
tags:
  - devops
  - blog
  - technical
---
The workflow of publishing in Substack automatically from the RSS feed of a GitHub page (that I published yesterday in [this article](https://anrodriguez.substack.com/p/how-to-write-articles-in-markdown-for-substack-and-medium-using-github-pages-atom-rss-feedshtml)) satisfies my needs.
## Missing image in my local and Substack, not on Github
Those with a keen eye, however, might have noticed that one of the images in the article was missing in Substack:

![](https://siran.github.io/assets/writing/missing-image-in-article.jpg)

*[The place of the missing image is pointed by the arrow (pointing to nothingness)](https://siran.github.io/assets/writing/missing-image-in-article.jpg)*

I did notice quite quickly that the image was missing from Substack; interestingly it showed on Github Pages. What a bummer, I thought. *What now?*
## Imgur was the problem
I slept it over, happy that the image failed to show in my local. That hinted to the solution.

Next day, I googled hotlinking from Imgur.

It turned out that Imgur has some restrictive policies to hotlink from blogs:

![](https://siran.github.io/assets/writing/hot-linking-from-imgur-not-allowed.png)

*[Imgur has some restrictive policies](https://siran.github.io/assets/writing/hot-linking-from-imgur-not-allowed.png)*
## Github pages as asset repository
It didn't took me long to realize that I could host the images in a Github page. And so, I did.

I created an `assets` repository on my GitHub and enabled GitHub Pages:

![](https://siran.github.io/assets/writing/enabling-git-hub-pages.png)

*[My assets repository in Github Pages](https://siran.github.io/assets/writing/enabling-git-hub-pages.png)*

Now, I can hotlink images from my blog (Substack, Medium, Dev.to, even GutHub pages itself) to my asset repository. For free I get version control of my assets and complete control over them (other than privacy, I guess, since it's a public read-only repository).

I hope GitHub pages remains free forever.

## Will GitHub Pages remain free forever for public repositories?
A quick peek seem to point it will be free - hopefully with hotlinking - forever:

![](https://siran.github.io/assets/writing/github-pages-free-forever.png)

*[It appears GitHub Pages is remaining free - hopefully with hotlinking](https://siran.github.io/assets/writing/github-pages-free-forever.png)*

However, in case it does not, it feels good to know that I have all my assets and articles locally saved and backup to the cloud.

## More automation needed for a more convenient article writing experience
All is about experience now a days (user experience, developer experience, etc-experience), and my current experience for image handling is not the best.

For each image in this article, I had to:

1. Take a screenshot
2. Save it to local directory (preferably with a "hyphened-name")
3. Add, commit and push to the repo
4. Build a link to the asset..

Phew! It's only 4 steps but for every image it's a hassle.

So I'll do a script to automate these tasks so I only have to 1) take screenshot 2) type regular name 3) paste into article.

I'll share more in the near future when it get's implemented.
