from google.cloud import aiplatform, storage
from src.configuration import set_configuration
from src.utils.constants import dataset_path
import os

project_id = set_configuration.PROJECT_ID
location = set_configuration.REGION
BUCKET_NAME = set_configuration.BUCKET_NAME
BUCKET_URI = set_configuration.BUCKET_URI


def create_and_import_dataset_tabular_gcs_sample(display_name):
    """
    Function to get input parameters and create dataset
    on vertex_ai platform using those parameters,
    @param display_name: dataset display name
    @return: response message
    """
    try:
        client = storage.Client()
        gcs_source = ""
        bucket = client.get_bucket(BUCKET_NAME)

        for filename in os.listdir(dataset_path):
            full_path = os.path.join(dataset_path, filename)
            if os.path.isfile(full_path):
                blob = bucket.blob(filename)
                blob.upload_from_filename(full_path)
                print(f'Uploaded {filename} to bucket {BUCKET_NAME}')

            gcs_source = f"{BUCKET_URI}/{filename}"

        dataset = aiplatform.TabularDataset.create(
            display_name=display_name,
            gcs_source=gcs_source,
        )

        dataset.wait()

        print(f'\tDataset: "{dataset.display_name}"')
        print(f'\tname: "{dataset.resource_name}"')
        print(f"Dataset Name: {dataset.display_name} created successfully.")

        return dataset

    except Exception as e:
        return e
