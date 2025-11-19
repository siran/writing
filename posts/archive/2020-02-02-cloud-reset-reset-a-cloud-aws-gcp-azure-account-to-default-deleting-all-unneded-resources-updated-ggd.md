---
title: >-
  Cloud-Reset: Reset a Cloud (AWS, GCP, Azure) account to default (deleting all
  unneded resources!)
date: '2020-02-02T18:07:16.049Z'
excerpt: >-
  Ever wanted to reset (delete all the resources) from a cloud account
  (AWS/GCP/...)? Now you can, and...
thumb_img_path: null
comments_count: 0
positive_reactions_count: 6
tags:
  - python
  - aws
  - devops
canonical_url: 'https://medium.com/@mrodz/reset-an-aws-account-to-default-889c0a0680f6'
layout: post
---
Ever wanted to reset (delete all the resources) from a cloud account (AWS/GCP/...)? Now you can, and its really easy.

![Easily throw away (DELETE) unneeded resources.](https://cdn-images-1.medium.com/max/800/1*kdHTfcAS7BMWWplNnMuI1w.png)
<figcaption>Easily throw away (DELETE) unneeded resources.</figcaption>

## Freedom
We want to give everyone the freedom to explore all what AWS has to offer. So we decided to create a 'sandbox' account where everybody could create any resource they want.

## Freedom has its cost

Of course, resources cost money. And as good as we are in giving everyone the freedom to explore, we didn't want to spend more money than necessary by having lingering zombie resources that nobody knew even existed.

So, we also wanted to delete all resources periodically.

This was more easily said than done.

## Solution

I tried finding some GitHub project that already did this, or at least that we could collaborate.

Although we found a couple (listed below in case you are interested), these we’re writting in Go and we’re too complicated to my test.

## The project

So I literally this afternoon started a GitHub open-source project to achieve this.

All types of resources are handled by its own class, so its easy to extend.

The filename where the class is names after the Boto3 resource name (ec2, ec2, ses, s3, etc…).

If you’re interested in this project, I’d love to see your collaborations. We can keep adding resources.

The first couple commits are a little messy, just because it’s the start of the project and it get hectic. But the idea is to keep it clean and tidy, tested and following best practices.

Here’s the [cloud-reset repo](https://github.com/siran/cloud-reset):

## Let’s disect a bit

There is a main script delete_resoures.py that instantiates class called CloudReset.

When instantiating the class, you have to pass the name of a YAML configuration file. For example, a file named resources_to_delete.yml can have the following contents. This is valid YAML and its specified to delete resources of type ec2 and s3:


```yaml
- aws_ec2:
- aws_s3:
    exclude:
        - Name: /-terraform-/ # regular expression
        - Name: /-xxx-/
    options:
        force: true           # deletes bucket contents
- aws_kms:
```


Down the river, this instantiates the class in the file 
`lib/modules/ec2.py`
 which takes care of finding the ids of all the ec2s and deleting them.

Notice that for resource 
`s3`
 it’s possible to filter the resources to be deleted. We can 
`exclude`
 resources with 
`Name`
 matching a regular expression.

The 
`ec2.py`
 file (or any other resource file) is quite simple. It inherits from the 
`BaseResource`
 class, which enforces to have at least 3 methods:

- get_resources()
- list_resources()
- delete_resources()

## How to run

Before calling the script, be sure to install the requirements:


```
pip3 install -r requirements.txt
```


The script can be called as:


```
python delete_resources.py -f resources_to_delete.yml
```


The script is configured with a 
`dry_run`
 flag set initially to 
`True`
, so it should not delete anything by default. But be careful anyways.

## Future plans

In the future, we’re planning to specify in the YAML configuration file options to filter by tags, creation date and more. Also we’d like to add other cloud providers as GCP or Azure.

If you like the idea, clone the repo and show what you’ve got. There are many things we can do.

That’s it for now, but I hope to know more about you!

[Full article here](https://medium.com/@mrodz/reset-an-aws-account-to-default-889c0a0680f6)

*[This post is also available on DEV.](https://dev.to/michrodz/cloud-reset-reset-a-cloud-aws-gcp-azure-account-to-default-deleting-all-unneded-resources-updated-ggd)*


<script>
const parent = document.getElementsByTagName('head')[0];
const script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.1.1/iframeResizer.min.js';
script.charset = 'utf-8';
script.onload = function() {
    window.iFrameResize({}, '.liquidTag');
};
parent.appendChild(script);
</script>    
