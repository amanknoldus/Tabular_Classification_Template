from src.pipeline.pipeline import InitiateMLPipeline


if __name__ == '__main__':
    pipeline_instance = InitiateMLPipeline()
    result = pipeline_instance.pipeline()
    print(result)
