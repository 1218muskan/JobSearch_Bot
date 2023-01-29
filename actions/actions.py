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
import json
import random
import datetime
from typing import Dict, Text, Any, List, Optional
import logging
from rasa_sdk.interfaces import Action
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
    ActionExecutionRejected
)
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict


logger = logging.getLogger(__name__)

class ActionInternship(Action):

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "internship_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""
        slots = ["kind_of_internship", "placeofwork", "domain_of_interest", "work_mode"]

        for slot in slots:
            if slot not in tracker.slots:
                dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
                return [SlotSet(slot, None)]
        


        kind_of_internship = tracker.get_slot("kind_of_internship")
        placeofwork = tracker.get_slot("placeofwork")
        domain_of_interest = tracker.get_slot("domain_of_interest")
        work_mode = tracker.get_slot("work_mode")

        # Search for the internship in DB
        # If found, return the internship
        # If not found, return None
        # If multiple found, return all of them in a list
        


        dispatcher.utter_message(text="We have received the following information:")
        dispatcher.utter_message(text="Kind of internship: {}".format(kind_of_internship))
        dispatcher.utter_message(text="Place of work: {}".format(placeofwork))
        dispatcher.utter_message(text="Domain of interest: {}".format(domain_of_interest))
        dispatcher.utter_message(text="Work mode: {}".format(work_mode))
        return [SlotSet(slot, None) for slot in slots]

# class ValidateInternship(FormValidationAction):
#     def validate_kind_of_internship(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate kind_of_internship value."""
#         if slot_value.lower() in ["paid", "unpaid"]:
#             return {"kind_of_internship": slot_value}
#         else:
#             dispatcher.utter_message(text="Please enter if you'd prefer paid or unpaid internships.", buttons=[{"title": "Paid", "entity": "kind_of_internship", "value": "paid"}, {"title": "Unpaid", "entity": "kind_of_internship", "value": "unpaid"}])
#             return {"kind_of_internship": None}

#     def validate_placeofwork(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate placeofwork value."""
#         return {"placeofwork": slot_value}


#     def validate_domain_of_interest(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate domain_of_interest value."""
#         return {"domain_of_interest": slot_value}

#     def validate_work_mode(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate work_mode value."""
#         if slot_value.lower() in ["online", "offline", "hybrid"]:
#             return {"work_mode": slot_value}
#         else:
#             dispatcher.utter_message(text="Please enter if you'd prefer online, offline or hybrid internships.", buttons=[{"title": "Online", "entity": "work_mode", "value": "online"}, {"title": "Offline", "entity": "work_mode", "value": "offline"}, {"title": "Hybrid", "entity": "work_mode", "value": "hybrid"}])
#             return {"work_mode": None}

# class ValidateJob(FormValidationAction):

#     def validate_placeofwork(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate placeofwork value."""
#         return {"placeofwork": slot_value}


#     def validate_domain_of_interest(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate domain_of_interest value."""
#         return {"domain_of_interest": slot_value}

#     def validate_work_mode(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate work_mode value."""
#         if slot_value.lower() in ["online", "offline", "hybrid"]:
#             return {"work_mode": slot_value}
#         else:
#             dispatcher.utter_message(text="Please enter if you'd prefer online, offline or hybrid jobs.", buttons=[{"title": "Online", "entity": "work_mode", "value": "online"}, {"title": "Offline", "entity": "work_mode", "value": "offline"}, {"title": "Hybrid", "entity": "work_mode", "value": "hybrid"}])
#             return {"work_mode": None}


# class ValidateOpportunity(FormValidationAction):
#     def validate_placeofwork(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate placeofwork value."""
#         return {"placeofwork": slot_value}


#     def validate_domain_of_interest(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate domain_of_interest value."""
#         return {"domain_of_interest": slot_value}

#     def validate_work_mode(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate work_mode value."""
#         if slot_value.lower() in ["online", "offline", "hybrid"]:
#             return {"work_mode": slot_value}
#         else:
#             dispatcher.utter_message(text="Please enter if you'd prefer online, offline or hybrid opportunity.", buttons=[{"title": "Online", "entity": "work_mode", "value": "online"}, {"title": "Offline", "entity": "work_mode", "value": "offline"}, {"title": "Hybrid", "entity": "work_mode", "value": "hybrid"}])
#             return {"work_mode": None}

#     def validate_type_of_opportunity(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate type_of_opportunity value."""
#         if slot_value.lower() in ["scholarship", "course", "fellowship", "conference"]:
#             return {"type_of_opportunity": slot_value}
#         else:
#             dispatcher.utter_message(text="Please enter if you'd like to look for scholarships, courses, conferences or fellowship.", buttons=[{"title": "Scholarship", "entity": "type_of_opportunity", "value": "scholarship"}, {"title": "Course", "entity": "type_of_opportunity", "value": "course"}, {"title": "Conference", "entity": "type_of_opportunity", "value": "conference"}, {"title": "Fellowship", "entity": "type_of_opportunity", "value": "fellowship"}])
#             return {"type_of_opportunity": None}

#     def validate_level_of_opportunity(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate level_of_opportunity value."""
#         if slot_value.lower() in ["local", "national", "international"]:
#             return {"level_of_opportunity": slot_value}
#         else:
#             dispatcher.utter_message(text="Please enter if you'd like to look for local, national or international opportunities.", buttons=[{"title": "Local", "entity": "level_of_opportunity", "value": "local"}, {"title": "National", "entity": "level_of_opportunity", "value": "national"}, {"title": "International", "entity": "level_of_opportunity", "value": "international"}])
#             return {"level_of_opportunity": None}

class ActionJob(Action):

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "job_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""
        slots = ["placeofwork", "domain_of_interest", "work_mode"]

        for slot in slots:
            if slot not in tracker.slots:
                dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
                return [SlotSet(slot, None)]
        
        placeofwork = tracker.get_slot("placeofwork")
        domain_of_interest = tracker.get_slot("domain_of_interest")
        work_mode = tracker.get_slot("work_mode")
        dispatcher.utter_message("We have received the following information:")
        dispatcher.utter_message("Place of work: {}".format(placeofwork))
        dispatcher.utter_message("Domain of interest: {}".format(domain_of_interest))
        dispatcher.utter_message("Work mode: {}".format(work_mode))

        #Search for job in DB
        #If found, return the job
        #If not found, return None
        #If multiple found, return all of them in a list


        return [SlotSet(slot, None) for slot in slots]

class ActionOpportunity(Action):

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "opportunity_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""
        slots = ["Type", "level", "placeofwork", "domain_of_interest", "work_mode"]

        for slot in slots:
            if slot not in tracker.slots:
                dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
                return [SlotSet(slot, None)]
        


        Type = tracker.get_slot("Type")
        level = tracker.get_slot("level")
        placeofwork = tracker.get_slot("placeofwork")
        domain_of_interest = tracker.get_slot("domain_of_interest")
        work_mode = tracker.get_slot("work_mode")

        # Search for the opportunity in DB
        # If found, return the opportunity
        # If not found, return None
        # If multiple found, return all of them in a list


        dispatcher.utter_message("We have received the following information:")
        dispatcher.utter_message("Type: {}".format(Type))
        dispatcher.utter_message("level: {}".format(level))
        dispatcher.utter_message("place of work: {}".format(placeofwork))
        dispatcher.utter_message("domain of interest: {}".format(domain_of_interest))
        dispatcher.utter_message("work mode: {}".format(work_mode))
        return [SlotSet(slot, None) for slot in slots]