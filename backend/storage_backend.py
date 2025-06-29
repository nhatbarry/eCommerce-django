from storages.backends.s3boto3 import S3Boto3Storage

class CloudflareR2PublicStorage(S3Boto3Storage):
    bucket_name = "media"
    custom_domain = "pub-4a404b4050c34e9fae705d05aa87820a.r2.dev"