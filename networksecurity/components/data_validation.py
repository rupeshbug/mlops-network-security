import sys
import os

from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from scipy.stats import ks_2samp
import pandas as pd

class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig):
        try:
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    
    