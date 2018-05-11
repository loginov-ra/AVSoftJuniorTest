
import json
import os
from ftplib import FTP


class FileUploader(object):
    def __init__(self, path_to_json='config.json'):
        self.path_to_json = path_to_json
        self.get_copy_arguments()

    def get_copy_arguments(self):
        with open(self.path_to_json, 'r') as json_file:
            json_data = json_file.read()
            parsed_object = json.loads(json_data)
            self.input_filename = parsed_object["inputFilename"]
            self.ftp_path = parsed_object["ftpPath"]

    def __str__(self):
        return str(self.input_filename) + ' -> ' + str(self.ftp_path)
