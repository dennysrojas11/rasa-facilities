# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

datafacilities =[
    {
        'location': "Ambato",
        'facility': "hospital",
        'address': "Av de Prueba y Otra",
    },
    {
        'location': "Ambato",
        'facility': "clinical",
        'address': "Av de Prueba y Av. Eloy Alfaro",
    },
    {
        'location': "Ambato",
        'facility': "laboratory",
        'address': "Av de Prueba y Av. Cevallos",
    },
    {
        'location': "Cuenca",
        'facility': "hospital",
        'address': "Av de Cuenca y calle de Cuenca",
    },
    {
        'location': "Riobamba",
        'facility': "clinical",
        'address': "Av de Riobamba y calle de Riobamba",
    },
]

def get_address(location, facility):
    for facilityResponse in datafacilities:
        if facilityResponse.get("facility") == facility and facilityResponse.get("location") == location:
            return facilityResponse.get("address")
    return ''


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        facility = tracker.get_slot("facility")
        location = tracker.get_slot("location")

        res = get_address(location, facility)

        dispatcher.utter_message(text=res)

        return []

