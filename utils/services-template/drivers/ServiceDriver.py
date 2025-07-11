import boto3
import botocore
import constants as _C

from services.Evaluator import Evaluator

###### TO DO #####
## Import modules that needed for this driver
## Example
## from services.ec2.drivers.Ec2SecGroup import Ec2SecGroup

###### TO DO #####
## Replace ServiceDriver with

class ServiceDriver(Evaluator):
    
    ###### TO DO #####
    ## Replace resource variable to meaningful name
    ## Modify based on your need
    def __init__(self, resource):
        super().__init__()
        self.init()

        ###### TO DO #####
        ## Replace 'None' to unique identifer for this resource
        ## It has to be a STRING
        self._resourceName = None
        return
    
    ###### TO DO #####
    ## Change the method name to meaningful name
    ## Check methods name must follow _check[Description]
    def _checkDescription(self):
        ###### TO DO #####
        ## Develop the checks logic here
        ## If the resources failed the rules, flag the resource as example below
        self.results['Rule Name'] = [-1, "Info for customer to identify the resource"]
        return