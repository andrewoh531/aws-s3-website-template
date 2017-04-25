#!/usr/bin/env python
from subprocess import call
import argparse
import boto3
import os

def create_origin_access_identity(hosted_zone):
    client = boto3.client('cloudfront')

    print("Creating origin access identity...")
    response = client.create_cloud_front_origin_access_identity(
        CloudFrontOriginAccessIdentityConfig={
            'CallerReference': hosted_zone,
            'Comment': 'Origin access identity for ' + hosted_zone
        }
    )

    return response['CloudFrontOriginAccessIdentity']

def create_cloudformation_stack(stack_name, stack_template_file, original_access_identity):

    print("Creating/updating cloudformation resources...")
    cwd = os.getcwd()
    call(["docker", "run", "--rm", "-v", cwd + ":/cwd", "-e", "AWS_ACCESS_KEY_ID", "-e", "AWS_SECRET_ACCESS_KEY", \
            "-e", "AWS_DEFAULT_REGION", "realestate/stackup:latest", stack_name, "up", "-t", stack_template_file, \
            "--override", "HostedZone=" + hosted_zone, "--override", "OriginAccessIdentity=" + original_access_identity['Id'], \
            "--override", "CanonicalUserId=" + original_access_identity['S3CanonicalUserId']])

# TODO If call to docker errors then this script should also error out.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create aws resources to host a static website")
    parser.add_argument("domainName", help="The domain name to configure in Route 53")
    args = parser.parse_args()
    hosted_zone = args.domainName

    original_access_identity = create_origin_access_identity(hosted_zone)
    create_cloudformation_stack(hosted_zone.replace(".", "-") + "-s3-website", "./cloudformation-templates/s3-website.yml", original_access_identity)
