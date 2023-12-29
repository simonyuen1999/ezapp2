#!/usr/bin/env python3
import os
import aws_cdk as cdk
from ezapp2.ezapp2_stack import Ezapp2Stack

app = cdk.App()
Ezapp2Stack(app, "Ezapp2Stack")
app.synth()
