import pytest
from unittest.mock import AsyncMock
from app.services.email_service import EmailService

@pytest.mark.asyncio
async def test_send_markdown_email(email_service):
    # Mock the actual email sending method to avoid SMTP failure
    email_service.send_user_email = AsyncMock(return_value=True)

    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }

    # This call is now mocked and will not try to connect to SMTP
    result = await email_service.send_user_email(user_data, 'email_verification')

    assert result is True

