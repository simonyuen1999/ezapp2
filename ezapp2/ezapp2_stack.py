import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_apigateway as apigw

from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class Ezapp2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Create a new S3 bucket
        self.bucket = s3.Bucket( self, "ezApp2Bucket", versioned=True)

        # Create a new Lambda function
        self.lambda_function = _lambda.Function(
            self,                                    # Parent   
            "ezApp2Lambda",                          # The name of the lambda
            code=_lambda.Code.from_asset("lambda"),  # Specify the lambda directory,
            handler="handler.handler",               # the handler file and the handler function
            runtime=_lambda.Runtime.PYTHON_3_9,
        )

        # Create a new API Gateway
        self.api_gateway = apigw.RestApi(self, "ezApp2Api")
        self.api_gateway.root.add_method("GET", apigw.LambdaIntegration(self.lambda_function))

        # example resource
        # queue = sqs.Queue(
        #     self, "Ezapp2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
