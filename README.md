# AWS S3 Website Template

This repository creates an S3 hosted website using cloudformation. The following AWS resources are created:
* Route 53 record sets
* A Cloudfront origin access identity to allow Cloudfront access to the S3 bucket
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
To create the stack run `./deploy.py --dns <website-dns-name> --hosted-zone <route-53-hosted-zone-name>`. For example if you're trying to create a website
with the DNS name of `dev.andrewoh.ninja` and a hosted zone value of `andrewoh.ninja` run the command `./deploy.sh --dns dev.andrewoh.ninja --hosted-zone andrewoh.ninja` and wait for all 
AWS resources to be created.

Note that you will need to create the hosted zone `andrewoh.ninja` prior to running the script.

## Deploying your website's html/css/js 
This script will create the necessary AWS resources however you will be responsible for deploying your website to the relevant S3 bucket using either aws cli or your own deployment strategy. You can run the `aws s3 sync` command to sync a specific directory to the s3 bucket. For example you can run
`aws s3 sync . s3://your-bucket-name` to sync the local directory with the bucket named `your-bucket-name`. You can retrieve the s3 bucket name from the Cloudformation template's resource list.

After you upload your files, you may need to invalidate the Cloudfront cache for the changes to be picked up.

