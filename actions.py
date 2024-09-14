from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os

class ActionProvideFilePath(Action):
    def name(self) -> str:
        return "action_provide_file_path"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        dispatcher.utter_message(text="Please provide the file path.")
        return []

class ActionReadFile(Action):
    def name(self) -> str:
        return "action_read_file"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        file_path = tracker.get_slot('file_path')
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            dispatcher.utter_message(text=f"File content: {content}")
        else:
            dispatcher.utter_message(text="File not found. Please provide a valid file path.")
        return []

class ActionCreateFile(Action):
    def name(self) -> str:
        return "action_create_file"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        file_name = tracker.get_slot('file_name')
        with open(file_name, 'w') as file:
            file.write("File created.")
        dispatcher.utter_message(text="File has been created successfully.")
        return []

class ActionUpdateFile(Action):
    def name(self) -> str:
        return "action_update_file"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        file_path = tracker.get_slot('file_path')
        file_content = tracker.get_slot('file_content')
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(f"\n{file_content}")
            dispatcher.utter_message(text="File has been updated successfully.")
        else:
            dispatcher.utter_message(text="File not found. Please provide a valid file path.")
        return []
