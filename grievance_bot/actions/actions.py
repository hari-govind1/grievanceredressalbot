# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionGetBlockNumber(Action):
    def name(self) -> Text:
        return "action_get_block_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        block_entity = next(tracker.get_latest_entity_values("block"), None)

        if block_entity:
            # Prepare data to append or create new JSON file
            extracted_entities = {"Issue Type": "Issue in infrastructure", "block_number": block_entity}
            json_file_path = "extracted_entities.json"

            # Read existing JSON data
            existing_data = []
            with open(json_file_path, "r") as json_file:
                existing_data = json.load(json_file)

            # Append new entity
            existing_data.append(extracted_entities)

            # Write updated data back to JSON file
            with open(json_file_path, "w") as json_file:
                json.dump(existing_data, json_file)

            dispatcher.utter_message(text=f"Your issue related with infrastructure has been reported in {block_entity}.")
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't recognize the block. Please provide a valid block.")

        return [] 

class ActionGetBusNumber(Action):
    def name(self) -> Text:
        return "action_get_bus_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bus_entity = next(tracker.get_latest_entity_values("bus_number"), None)

        if bus_entity:
            # Prepare data to append or create new JSON file
            extracted_entities = {"Issue Type": "Issue in bus", "bus_number": bus_entity}
            json_file_path = "extracted_entities.json"

            # Read existing JSON data
            existing_data = []
            with open(json_file_path, "r") as json_file:
                existing_data = json.load(json_file)

            # Append new entity
            existing_data.append(extracted_entities)

            # Write updated data back to JSON file
            with open(json_file_path, "w") as json_file:
                json.dump(existing_data, json_file)

            dispatcher.utter_message(text=f"The issue with bus number: {bus_entity} is reported to college management.")
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't recognize the bus number. Please provide a valid bus number.")

        return []

class ActionGetLabInfo(Action):
    def name(self) -> Text:
        return "action_get_lab_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        lab_entity = next(tracker.get_latest_entity_values("lab_info"), None)

        if lab_entity:
            # Prepare data to append or create new JSON file
            extracted_entities = {"Issue Type": "Issue in lab", "lab_info": lab_entity}
            json_file_path = "extracted_entities.json"

            # Read existing JSON data
            existing_data = []
            with open(json_file_path, "r") as json_file:
                existing_data = json.load(json_file)

            # Append new entity
            existing_data.append(extracted_entities)

            # Write updated data back to JSON file
            with open(json_file_path, "w") as json_file:
                json.dump(existing_data, json_file)

            dispatcher.utter_message(text=f"The issue in lab:{lab_entity} is reported is reported to college management.")
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't recognize the lab. Please provide a valid lab number or name.")

        return []


