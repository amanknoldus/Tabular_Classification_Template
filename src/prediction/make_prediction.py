import numpy as np
from google.cloud import aiplatform

from src.configuration import set_configuration
from src.prediction import instances_data

PROJECT_ID = set_configuration.PROJECT_ID
REGION = set_configuration.REGION


def get_prediction(
        instances=instances_data.instances_parameter
):
    """
    Function to get online prediction by passing instances to deployed ml model
    @param instances: input parameters
    @return:  prediction result
    """
    try:

        client = aiplatform.gapic.EndpointServiceClient(
            client_options={"api_endpoint": f"{REGION}-aiplatform.googleapis.com"})

        endpoints = client.list_endpoints(parent=f"projects/{PROJECT_ID}/locations/{REGION}")

        endpoint_id = ''
        for endpoint in endpoints:
            endpoint_id = endpoint.name.split("/")[-1]

        aiplatform.init(project=PROJECT_ID, location=REGION)
        endpoint = aiplatform.Endpoint(endpoint_id)

        prediction = endpoint.predict(instances=instances)
        data = np.array(prediction[0])
        data_dictionary = data[0]
        classes = data_dictionary['classes']
        scores = data_dictionary['scores']

        return f"Classes: {classes}, Confidence Score: {scores}"

    except Exception as e:
        return e
