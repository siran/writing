---
title: Use MFA on the CLI and execute awscli commands securely
excerpt: You can script your way through secure convenience.
date: 2020-02-03T01:46:35.394Z
tags:
  - aws
  - scripting
canonical_url: https://anrodriguez.substack.com/p/use-mfa-on-the-cli-and-execute-awscli-commands-securely-3i8chtml
layout: post
---
[![u-https-insidesmallbusiness-com-au-wp-content-uploads-2019-03.jpg](https://i.postimg.cc/Mpf8NMF0/u-https-insidesmallbusiness-com-au-wp-content-uploads-2019-03.jpg)](https://postimg.cc/PCHc8xhN)

To enhance security, you can enable multi-factor authenticantion (MFA) use also for issuing CLI commands. Manually obtaining the temporary tokens and setting them up as environment variables can be a hassle. I came up with this quick script to automate the job.

In the following script, you only have to replace
`YOUR_MFA_ARN`
 with the MFA device you have configured in you security settings in your AWS IAM user.

Then you can either
`source`
 or
`execute`
 the script.

[Here's the bash script
`aws-mfa-cli.sh`
](https://gist.github.com/siran/0979d1f9aeaa16e7fa7162e16ded6f19):


```bash
# !/bin/bash
set -e

# check if script has been sourced or executed
(return 0 2>/dev/null) && sourced=1 || sourced=0

MFA_DEVICE_ARN=YOUR_MFA_ARN

read -p "Please enter you MFA code: " MFA_CODE

echo "You entered '$MFA_CODE'"

echo aws --output text sts get-session-token \
    --serial-number arn:aws:iam::661095214357:mfa/anmichel.rodriguez@annalect.com \
    --token-code $MFA_CODE

CREDS=$(aws --output text sts get-session-token \
    --serial-number $MFA_DEVICE_ARN \
    --token-code $MFA_CODE)

echo $CREDS

KEY=$(echo $CREDS | cut -d" " -f2)
SECRET=$(echo $CREDS | cut -d" " -f4)
SESS_TOKEN=$(echo $CREDS | cut -d" " -f5)

echo "Key: $KEY"
echo "Secret: $SECRET"
echo "Session token: $SESS_TOKEN"

export AWS_ACCESS_KEY_ID=$KEY
export AWS_SECRET_ACCESS_KEY=$SECRET
export AWS_SESSION_TOKEN=$SESS_TOKEN

if [ $sourced -eq 1 ]; then
    echo "Script was sourced."
else
    echo "Script was executed, starting subshell."
    bash -l
fi
```


*[This post is also available on DEV.](https://dev.to/michrodz/use-mfa-on-the-cli-and-execute-awscli-commands-securely-3i8c)*


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
