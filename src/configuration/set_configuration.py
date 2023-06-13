import subprocess

PROJECT_ID = "phonic-chemist-389211"  # specify project id
REGION = "us-central1"  # specify region name
BUCKET_NAME = "phonic-chemist-389211"  # specify bucket name
BUCKET_URI = f"gs://{PROJECT_ID}"

command_list = ["gcloud auth application-default login",
                f"gcloud config set project {PROJECT_ID}",
                f"gsutil mb -l {REGION} {BUCKET_URI}"
                ]


def run_command():
    """
    Function to set your Google Account Login,
    Set Vertex AI Project, Create Bucket to store data into it.
    @return: response message
    """
    try:
        for command in command_list:
            subprocess.call(command, shell=True)

    except Exception as e:
        print(e)

# run_command()
# un-comment this above line to run this current file
