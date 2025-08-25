# website/supabase_utils.py

import os
from supabase import create_client, Client
from django.core.files.uploadedfile import InMemoryUploadedFile

def upload_to_supabase(file: InMemoryUploadedFile, model_name: str):
    """
    Uploads a file to Supabase Storage and returns the public URL.

    Args:
        file: The in-memory uploaded file from a Django form.
        model_name: The name of the model (e.g., 'case_studies', 'team').
    
    Returns:
        The public URL of the uploaded file, or None if upload fails.
    """
    try:
        # Get credentials from environment variables
        supabase_url = os.environ.get('SUPABASE_PROJECT_URL')
        supabase_key = os.environ.get('SUPABASE_SERVICE_KEY')
        bucket_name = 'anantastorage' # The name of your public bucket

        if not all([supabase_url, supabase_key]):
            print("Error: Supabase credentials are not set in environment variables.")
            return None

        # Initialize Supabase client
        supabase: Client = create_client(supabase_url, supabase_key)
        
        # Define the path for the file inside the bucket
        # e.g., case_studies/my-image.jpg
        file_path_in_bucket = f"{model_name}/{file.name}"

        # Upload the file
        # We must use file.read() to get the binary content
        supabase.storage.from_(bucket_name).upload(
            path=file_path_in_bucket,
            file=file.read(),
            file_options={"content-type": file.content_type}
        )

        # Get the public URL
        public_url = supabase.storage.from_(bucket_name).get_public_url(file_path_in_bucket)
        
        print(f"Successfully uploaded {file.name} to Supabase.")
        return public_url

    except Exception as e:
        print(f"Error uploading file to Supabase: {e}")
        return None