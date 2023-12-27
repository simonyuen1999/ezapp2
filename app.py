from aws_cdk_lib import core as cdk
from ezapp2.ezapp2_stack import Ezapp2Stack

app = cdk.App()
Ezapp2Stack(app, "Ezapp2Stack")
app.synth()
