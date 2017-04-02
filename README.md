# AWS Website Deployment for MyNiche.com.au #

This repository is a bunch of helper scripts to aid in the deployment of a static website hosted on S3.

It utilizes:
* Cloudformation ([template retrieved and slightly modified and converted from JSON to YAML](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-services-us-west-2.html#w1ab2c21c45c15c33))
* Stackup (via docker)

This repo is optimised and configured for the `mynich.com.au` website. 

## Prerequisites ##

You will need python version 3. You will also need to install the python dependencies by running:
`pip install -r requirements.txt`.

You will need to install Docker.

You will also need the following environment variables set as they are used by Stackup (via Docker):
```
export AWS_DEFAULT_REGION=ap-southeast-2
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=yyy
```

To deploy changes to the website
move the whole website (all static files and assets) into the `./website-artifacts/` folder then run the `deploy.sh` script.