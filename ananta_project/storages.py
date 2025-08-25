# ananta_project/storages.py

from storages.backends.s3boto3 import S3Boto3Storage
import os

class SupabaseMediaStorage(S3Boto3Storage):
    # Get credentials directly from environment variables
    access_key = os.environ.get('SUPABASE_PROJECT_ID')
    secret_key = os.environ.get('SUPABASE_SERVICE_KEY')
    bucket_name = 'anantastorage' # Your bucket name
    
    # Supabase requires a specific endpoint URL
    endpoint_url = os.environ.get('SUPABASE_S3_ENDPOINT_URL')
    
    # These are important settings for Supabase
    location = '' # Save files at the root of the bucket
    file_overwrite = False
    default_acl = 'public-read'
    querystring_auth = False # Important for generating clean public URLs
    
    # This generates the correct public URL for your files
    @property
    def custom_domain(self):
        if self.endpoint_url:
            return f"{self.access_key}.supabase.co/storage/v1/object/public/{self.bucket_name}"
        return None