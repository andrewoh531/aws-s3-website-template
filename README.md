# Generic AWS S3 Website Template #

This repository is a bunch of helper scripts to aid in the deployment of a static website hosted on S3.

It utilizes:
* Cloudformation ([template retrieved and slightly modified and converted from JSON to YAML](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-services-us-west-2.html#w1ab2c21c45c15c33))
* Stackup (via docker)

The following AWS resources are created:
* Route 53 record sets
* Cloudfront distribution (along with its Origin Access Identity)
* S3 bucket (and necessarily bucket policy to ensure objects can only be accessed via Cloudfront)

## Prerequisites ##

1. You will need python version 3. You will also need to install the python dependencies by running: `pip install -r requirements.txt`.
2. You will need to install Docker.
3. You will need to have the Route 53 hosted zone created for the Record sets to be created
4. You will also need the following environment variables set as they are used by Stackup (via Docker):
```
export AWS_DEFAULT_REGION=ap-southeast-2
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=yyy
```

## Creating the stack
To create the stack run `./deploy.sh <domain-name>`. For example if you're trying to create a website
with the root apex dns of `andrewoh.ninja` run the command `./deploy.sh andrewoh.ninja` and wait for all 
AWS resources to be created.


## Deploying your website's html/css/js 
This script will create the necessary AWS resources however you will be responsible for deploying your website to the relevant S3 bucket
using either aws cli or your own deployment strategy. Deploying your website is outside the scope of this repository.

## TODO
The origin access identity configuration may not be quite correct. Have created a new stack with this template and
have been getting `Access denied` errors from S3. This will need to be revisited.