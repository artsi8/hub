import json
from typing import List

import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_api_gateway import StoreGateway

class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]) -> bool:
        """"Надсилання оброблених даних у Store API
        :param processed_agent_data_batch: List[ProcessedAgentData]
        :return:  True, якщо дані успішно надіслано
        """
        # Make a POST request to the Store API endpoint with the processed data
        data_to_save = []
        for data_item in processed_agent_data_batch:
            json_string = data_item.json()
            # print(f"JSON string: {json_string}")
            data_item_dict = json.loads(json_string)
            # print(f"Data item dict: {data_item_dict}")
            data_to_save.append(data_item_dict)

        api_endpoint = f"{self.api_base_url}/processed_agent_data/"
        api_response = requests.post(api_endpoint, json=data_to_save)
        print("from save_data: +")
        return api_response.status_code == requests.codes.ok
