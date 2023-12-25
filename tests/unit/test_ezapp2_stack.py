import aws_cdk as core
import aws_cdk.assertions as assertions

from ezapp2.ezapp2_stack import Ezapp2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in ezapp2/ezapp2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Ezapp2Stack(app, "ezapp2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
