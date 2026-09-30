import pytest

from validators import is_valid_email


@pytest.mark.parametrize(
	"email",
	[
		"user@example.com",
		"user@mail.example.com",
		"user+tag@example.com",
	],
)
def test_normal_email_cases(email):
	assert is_valid_email(email) is True


@pytest.mark.parametrize(
	"email",
	[
		"userexample.com",
		"user@",
		"@example.com",
		"user@example",
		"user..name@example.com",
		"user name@example.com",
	],
)
def test_negative_email_cases(email):
	assert is_valid_email(email) is False


@pytest.mark.parametrize("email", ["", None, 12345])
def test_edge_email_cases(email):
	assert is_valid_email(email) is False


def test_rejects_multiple_at_symbols():
	assert is_valid_email("user@@example.com") is False
