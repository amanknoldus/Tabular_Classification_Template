This Template represents a machine learning mode pipeline for creating a classification job, please follow the below step to create your own pipeline.

# Enable Vertex AI api service via this below link:
# https://console.cloud.google.com/apis/library/aiplatform.googleapis.com

Install following libraries:
    >> pip install virtualenv
    >> pip install google-cloud-aiplatform

Enable following permissions in your Vertex AI Service Account:
    >> IAM and admin >> click on grant access button >> Input your service account in New principals field >> Select a role >> select options:
        Owner, Editor, AutoML Predictor, AI Platform Viewer, Vertex AI User, Vertex AI Feature Store data viewer, Vertex AI Feature Store data writer,
        Vertex AI Feature Store admin.
        

Step 1: Go to file > src/configuration/set_configuration > change your parameters according to your project details and run as current file,

Step 2: Go to folder > ser/dataset_directory > replace with your dataset,

Step 3: Go to file > src/prediction/instances_data > change parameters according to your use case as input features used from your dataset for training,

Step 4: Now run "main.py" file,

Step 5: Now in terminal enter your dataset display name of your choice("your dataset will be created over cloud"),

Step 6: Now enter your training pipeline display name("wait for a while until your training finishes"),

Step 7: Now enter the name for deploying your model to an endpoint(wait for a while unit your model get deployed),

Step 8: Go to file > src/prediction/instances_data > change parameters according to your use case as input features used from your dataset for training,
        #this step can also be done in advance if you are sure about your training features.

Final Step 9: Now get your prediction as result.
