# tests/test_api.py
import requests
import sys
import time

BASE_URL = "http://localhost:8000/tickets"

# A simple dictionary to share data between tests
test_data = {}

def run_test(test_func):
    """Decorator to run a test and print its status."""
    try:
        test_func()
        print(f"✅ PASSED: {test_func.__name__}")
        return True
    except Exception as e:
        print(f"❌ FAILED: {test_func.__name__}\n   Error: {e}")
        return False

@run_test
def test_generate_ticket():
    """Tests the POST /generate endpoint."""
    payload = {"event_id": 1, "owner_name": "John Doe", "price": 99.99}
    response = requests.post(f"{BASE_URL}/generate", json=payload)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert "id" in data
    assert "qr_code" in data
    assert data["owner_name"] == "John Doe"
    
    # Save generated data for subsequent tests
    test_data['ticket_id'] = data['id']
    test_data['qr_code'] = data['qr_code']
    test_data['event_id'] = data['event_id']
    print(f"   -> Generated ticket ID: {data['id']}, QR Code: {data['qr_code']}")

@run_test
def test_get_ticket_by_id():
    """Tests the GET /{ticket_id} endpoint."""
    ticket_id = test_data['ticket_id']
    response = requests.get(f"{BASE_URL}/{ticket_id}")
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()['id'] == ticket_id

@run_test
def test_get_tickets_by_event():
    """Tests the GET /event/{event_id} endpoint."""
    event_id = test_data['event_id']
    response = requests.get(f"{BASE_URL}/event/{event_id}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "Event should have at least one ticket"
    assert data[0]['event_id'] == event_id

@run_test
def test_validate_ticket_successfully():
    """Tests a successful ticket validation."""
    qr_code = test_data['qr_code']
    response = requests.post(f"{BASE_URL}/validate", json={"qr_code": qr_code})
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()['message'] == "Ticket validated successfully"

@run_test
def test_validate_used_ticket():
    """Tests validating a ticket that has already been used."""
    qr_code = test_data['qr_code']
    # The service logic should mark the ticket as used, so a second attempt should fail
    response = requests.post(f"{BASE_URL}/validate", json={"qr_code": qr_code})
    
    assert response.status_code == 400, f"Expected 400 for used ticket, got {response.status_code}"
    assert "Invalid or already used ticket" in response.json()['detail']

@run_test
def test_get_nonexistent_ticket():
    """Tests getting a ticket that does not exist."""
    response = requests.get(f"{BASE_URL}/999999")
    assert response.status_code == 404, f"Expected 404 for non-existent ticket, got {response.status_code}"


if __name__ == "__main__":
    print("--- Starting API Integration Tests ---")
    
    # Wait a moment for the server to be fully ready
    time.sleep(5) 
    
    results = [
        test_generate_ticket,
        test_get_ticket_by_id,
        test_get_tickets_by_event,
        test_validate_ticket_successfully,
        test_validate_used_ticket,
        test_get_nonexistent_ticket
    ]
    
    if all(results):
        print("\n🎉 All tests passed successfully!")
        sys.exit(0)
    else:
        print("\n🔥 Some tests failed.")
        sys.exit(1)
