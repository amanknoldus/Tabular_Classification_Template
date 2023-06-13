from google.cloud import aiplatform
from src.configuration import set_configuration

PROJECT_ID = set_configuration.PROJECT_ID
REGION = set_configuration.REGION


def get_training(DISPLAY_NAME, TARGET_COLUMN, DATASET):
    """
    Function to get training input parameters and start training job on vertex_ai
    @param DATASET: dataset info
    @param TARGET_COLUMN: target(dependent) feature name
    @param DISPLAY_NAME: training model display name
    @return: response message

    """
    try:

        job = aiplatform.AutoMLTabularTrainingJob(
            display_name=DISPLAY_NAME,
            optimization_prediction_type="classification",
        )

        model = job.run(
            dataset=DATASET,
            target_column=TARGET_COLUMN,
            training_fraction_split=0.8,
            validation_fraction_split=0.1,
            test_fraction_split=0.1,
            budget_milli_node_hours=1000,
            model_display_name=DISPLAY_NAME,
            disable_early_stopping=False,
        )

        return "Model Trained Successfully"

    except Exception as e:
        return e
