# Generic AWS S3 Website Template #

This repository creates an S3 hosted website using cloudformation. The following AWS resources are created:
* Route 53 record sets
* Cloudfront distribution (along with its Origin Access Identity)
* S3 bucket (and necessarily bucket policy to ensure objects can only be accessed via Cloudfront)

## Prerequisites ##

1. You will need python version 3. You will also need to install the python dependencies by running: `pip install -r requirements.txt`.
2. You will need to install Docker.
3. You will need to have the Route 53 hosted zone created for the Record sets to be created
4. You will also need the following environment variables set as they are used by Stackup (via Docker):
```
export AWS_DEFAULT_REGION=region
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=yyy
```

## Creating the stack
To create the stack run `./deploy.sh <domain-name>`. For example if you're trying to create a website
with the domain name of `dev.andrewoh.ninja` run the command `./deploy.sh dev.andrewoh.ninja` and wait for all 
AWS resources to be created. Note that you will need to create the hosted zone `andrewoh.ninja` prior to running 
the script.

## Deploying your website's html/css/js 
This script will create the necessary AWS resources however you will be responsible for deploying your website to the relevant S3 bucket using either aws cli or your own deployment strategy. Deploying your website is outside the scope of this repository.
