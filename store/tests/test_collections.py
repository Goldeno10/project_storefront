from rest_framework.test import APIClient
from rest_framework import status
import pytest

class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        #Every test should have 3 parts, the triple As (Arrange, Act, Assert
        #Arrange: this is where we prepare a system under test, where we create objects
        # and put and database in an initial state and so on.
        #Act:  this is where we kick off the behaviour we want to test, in this case it is where we
        # send the request to the server
        
        #================Arrange==================
        #in this our case we dont use this 
        #===============Act======================
        client = APIClient()
        response = client.post('/store/collections/', {'tittle': 'a'})
        #==============Assert===================
        assert response == status.HTTP_401_UNAUTHORIZED
   
   
        