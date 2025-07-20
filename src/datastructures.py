"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Check if the member dictionary already has an "id" key
        if "id" not in member:
            # If not, generate a new id for the member
            member["id"] = self._generate_id()
        # Check if the member dictionary already has a "last_name" key
        if "last_name" not in member:
            # If not, set the last_name to the family's last_name
            member["last_name"] = self.last_name
        # Append the member dictionary to the _members list
        self._members.append(member)

    def delete_member(self, id):
        # Enumerate over the members list to get both index and member dictionary
        for i, m in enumerate(self._members):
            # Check if the id of the current member matches the given id
            if m["id"] == id:
                # If a match is found, remove the member from the list
                del self._members[i]
                return True
        # Return False if no member with the given id was found
        return False

    def get_member(self, id):
        # Loop through all member dictionaries in the _members list
        for m in self._members:
            # Check if the id of the current member matches the given id
            if m["id"] == id:
                # If a match is found, return the member dictionary
                return m
        # Return None if no member with the given id was found
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

jackson_family = FamilyStructure("Jackson")

