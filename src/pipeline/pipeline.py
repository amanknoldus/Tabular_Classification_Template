from google.cloud import aiplatform

from src.configuration import set_configuration
from src.dataset.create_dataset import create_and_import_dataset_tabular_gcs_sample
from src.deploy.deploy_model import deploy_model
from src.prediction.make_prediction import get_prediction
from src.training.training import get_training

PROJECT_ID = set_configuration.PROJECT_ID
REGION = set_configuration.REGION

aiplatform.init(project=PROJECT_ID, location=REGION)


class InitiateMLPipeline:

    def pipeline(self):
        try:

            # dataset = self.get_dataset()
            #
            # model_training_result = self.get_training(dataset)
            # print(model_training_result)

            deployed_model_result = self.get_deploy_model()
            print(deployed_model_result)

            prediction_result = self.get_predict()
            return prediction_result

        except Exception as e:
            return str(e)

    @staticmethod
    def get_dataset():
        """
        Function to get dataset input parameters from user,
        and pass it to dataset creation function to create dataset on vertex_ai platform
        @return: dataset input parameters
        """
        try:
            print("\nPlease Provide Inputs to Create Your Dataset: \n")

            dataset_display_name = input("Enter Dataset Display Name: \n")

            result = create_and_import_dataset_tabular_gcs_sample(dataset_display_name)
            return result

        except:
            raise RuntimeError

    @staticmethod
    def get_training(DATASET):
        """
        Function to get create training pipeline from user and pass it to
        get_training function to initiate training job
        @return: response message
        """
        try:
            print("Please Provide Inputs to Create Your Training Pipeline: \n")
            display_name = input("Enter Display Name: \n")
            target_col_name = input('Enter Target Columns: \n')

            result = get_training(display_name,
                                  target_col_name, DATASET)
            return result

        except:
            raise RuntimeError

    @staticmethod
    def get_deploy_model():
        """
        Function to pass model display name and deploy model to cloud
        @return: response message
        """
        try:
            print("Please Provide Inputs to Deploy Your Model To Endpoint: \n")
            deployed_display_name = input("Enter Deployed Model Display Name: \n")

            result = deploy_model(deployed_display_name)
            return result
        except:
            raise RuntimeError

    @staticmethod
    def get_predict():
        """
        Function to get prediction result from get_prediction function
        @return: prediction result
        """
        try:
            result = get_prediction()
            return result

        except:
            raise RuntimeError
