"""
Tests for the unregister functionality of the Mergington High School API.
"""
import pytest
from fastapi import status


class TestUnregisterEndpoint:
    """Test activity unregister functionality."""

    def test_unregister_successful(self, client):
        """Test successful unregistration from an activity."""
        # First, signup a user
        activity_name = "Math Club"
        email = "test@mergington.edu"
        
        signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert signup_response.status_code == status.HTTP_200_OK
        
        # Then unregister them
        unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
        assert unregister_response.status_code == status.HTTP_200_OK
        
        result = unregister_response.json()
        assert "message" in result
        assert email in result["message"]
        assert activity_name in result["message"]
        assert "unregistered" in result["message"].lower()

    def test_unregister_user_not_registered(self, client):
        """Test unregistering a user who is not registered for the activity."""
        activity_name = "Math Club"
        email = "notregistered@mergington.edu"
        
        response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        result = response.json()
        assert "not signed up" in result["detail"].lower()

    def test_unregister_nonexistent_activity(self, client):
        """Test unregistering from an activity that doesn't exist."""
        activity_name = "Nonexistent Activity"
        email = "test@mergington.edu"
        
        response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
        result = response.json()
        assert "not found" in result["detail"].lower()

    def test_unregister_existing_participant(self, client):
        """Test unregistering an existing participant from the sample data."""
        # Use Chess Club which has existing participants
        activity_name = "Chess Club"
        email = "michael@mergington.edu"  # This user exists in the sample data
        
        response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
        assert response.status_code == status.HTTP_200_OK
        
        result = response.json()
        assert "unregistered" in result["message"].lower()
        
        # Verify the user is no longer in the participants list
        activities_response = client.get("/activities")
        activities = activities_response.json()
        chess_club_participants = activities["Chess Club"]["participants"]
        assert email not in chess_club_participants

    def test_signup_and_unregister_workflow(self, client):
        """Test the complete workflow of signing up and then unregistering."""
        activity_name = "Science Club"
        email = "workflow@mergington.edu"
        
        # Check initial state
        initial_response = client.get("/activities")
        initial_activities = initial_response.json()
        initial_count = len(initial_activities[activity_name]["participants"])
        
        # Sign up
        signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert signup_response.status_code == status.HTTP_200_OK
        
        # Verify signup worked
        after_signup_response = client.get("/activities")
        after_signup_activities = after_signup_response.json()
        after_signup_count = len(after_signup_activities[activity_name]["participants"])
        assert after_signup_count == initial_count + 1
        assert email in after_signup_activities[activity_name]["participants"]
        
        # Unregister
        unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
        assert unregister_response.status_code == status.HTTP_200_OK
        
        # Verify unregister worked
        after_unregister_response = client.get("/activities")
        after_unregister_activities = after_unregister_response.json()
        after_unregister_count = len(after_unregister_activities[activity_name]["participants"])
        assert after_unregister_count == initial_count
        assert email not in after_unregister_activities[activity_name]["participants"]

    def test_unregister_url_encoding(self, client):
        """Test that activity names and emails with special characters are handled correctly."""
        # Test with spaces and special characters
        activity_name = "Programming Class"  # Contains space
        email = "user+test@mergington.edu"  # Contains special character
        
        # First signup
        signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert signup_response.status_code == status.HTTP_200_OK
        
        # Then unregister
        unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
        assert unregister_response.status_code == status.HTTP_200_OK