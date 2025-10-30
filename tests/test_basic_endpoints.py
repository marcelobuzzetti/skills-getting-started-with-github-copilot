"""
Tests for the basic API endpoints of the Mergington High School API.
"""
import pytest
from fastapi import status


class TestBasicEndpoints:
    """Test basic API endpoints."""

    def test_root_redirects_to_static(self, client):
        """Test that root endpoint redirects to static HTML."""
        response = client.get("/", follow_redirects=False)
        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
        assert response.headers["location"] == "/static/index.html"

    def test_get_activities_returns_all_activities(self, client):
        """Test that GET /activities returns all activities."""
        response = client.get("/activities")
        assert response.status_code == status.HTTP_200_OK
        
        activities = response.json()
        assert isinstance(activities, dict)
        assert len(activities) > 0
        
        # Check that Chess Club exists (from our sample data)
        assert "Chess Club" in activities
        assert "description" in activities["Chess Club"]
        assert "schedule" in activities["Chess Club"]
        assert "max_participants" in activities["Chess Club"]
        assert "participants" in activities["Chess Club"]

    def test_get_activities_structure(self, client):
        """Test that activities have the correct structure."""
        response = client.get("/activities")
        activities = response.json()
        
        for activity_name, activity_data in activities.items():
            assert isinstance(activity_name, str)
            assert isinstance(activity_data, dict)
            
            # Check required fields
            required_fields = ["description", "schedule", "max_participants", "participants"]
            for field in required_fields:
                assert field in activity_data, f"Missing field {field} in activity {activity_name}"
            
            # Check data types
            assert isinstance(activity_data["description"], str)
            assert isinstance(activity_data["schedule"], str)
            assert isinstance(activity_data["max_participants"], int)
            assert isinstance(activity_data["participants"], list)