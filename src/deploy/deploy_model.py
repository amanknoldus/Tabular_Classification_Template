from google.cloud import aiplatform, aiplatform_v1beta1
from src.configuration import set_configuration

PROJECT_ID = set_configuration.PROJECT_ID
REGION = set_configuration.REGION


def deploy_model(
        model_display_name=str,
        machine_type='e2-standard-2',
        sync: bool = True,
):
    """
    Function to deploy ml model to a endpoint
    @param model_display_name: name of deployed model
    @param machine_type: machine type used by model
    @param sync: sync setting enabled
    @return: response message
    """
    try:
        client = aiplatform.gapic.ModelServiceClient(
            client_options={"api_endpoint": f"{REGION}-aiplatform.googleapis.com"})
        parent = f"projects/{PROJECT_ID}/locations/{REGION}"

        response = client.list_models(parent=parent)

        model_id = ''
        for model in response:
            model_id = model.name.split("/")[-1]

        model_name = f"projects/{PROJECT_ID}/locations/{REGION}/models/{model_id}"

        aiplatform.init(project=PROJECT_ID, location=REGION)

        model = aiplatform.Model(model_name=model_name)

        model.enable_feature_attributions = True

        model.deploy(
            deployed_model_display_name=model_display_name,
            min_replica_count=1,
            max_replica_count=1,
            machine_type=machine_type,
            sync=sync,
        )
        model.enable_feature_attributions = True
        aiplatform.gapic.ModelServiceClient().update_model(model=model)

        model.wait()

        print(model.display_name)
        print(model.resource_name)
        if model:
            return "Model Deployed Successfully"

    except Exception as e:
        return e
