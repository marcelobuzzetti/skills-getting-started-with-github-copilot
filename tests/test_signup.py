"""
Tests for the signup functionality of the Mergington High School API.
"""
import pytest
from fastapi import status


class TestSignupEndpoint:
    """Test activity signup functionality."""

    def test_signup_successful(self, client):
        """Test successful signup for an activity."""
        # Use an activity that exists and has space
        activity_name = "Math Club"
        email = "test@mergington.edu"
        
        response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert response.status_code == status.HTTP_200_OK
        
        result = response.json()
        assert "message" in result
        assert email in result["message"]
        assert activity_name in result["message"]

    def test_signup_duplicate_user(self, client):
        """Test that signing up the same user twice fails."""
        activity_name = "Math Club"
        email = "test@mergington.edu"
        
        # First signup should succeed
        response1 = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert response1.status_code == status.HTTP_200_OK
        
        # Second signup should fail
        response2 = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
        
        result = response2.json()
        assert "already signed up" in result["detail"].lower()

    def test_signup_nonexistent_activity(self, client):
        """Test signup for an activity that doesn't exist."""
        activity_name = "Nonexistent Activity"
        email = "test@mergington.edu"
        
        response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
        result = response.json()
        assert "not found" in result["detail"].lower()

    def test_signup_activity_full(self, client):
        """Test signup when activity is at capacity."""
        # First, get an activity and fill it to capacity
        activities_response = client.get("/activities")
        activities = activities_response.json()
        
        # Find an activity with limited spots
        activity_name = "Chess Club"  # This has max_participants = 12
        activity_data = activities[activity_name]
        
        # Calculate how many more participants we can add
        current_participants = len(activity_data["participants"])
        max_participants = activity_data["max_participants"]
        spots_left = max_participants - current_participants
        
        # Fill up the remaining spots
        for i in range(spots_left):
            email = f"test{i}@mergington.edu"
            response = client.post(f"/activities/{activity_name}/signup?email={email}")
            assert response.status_code == status.HTTP_200_OK
        
        # Now try to add one more participant - should fail
        overflow_email = "overflow@mergington.edu"
        response = client.post(f"/activities/{activity_name}/signup?email={overflow_email}")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        result = response.json()
        assert "full" in result["detail"].lower()

    def test_signup_url_encoding(self, client):
        """Test that activity names and emails with special characters are handled correctly."""
        # Test with spaces and special characters in activity name
        activity_name = "Programming Class"  # Contains space
        email = "user+test@mergington.edu"  # Contains special character
        
        response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert response.status_code == status.HTTP_200_OK