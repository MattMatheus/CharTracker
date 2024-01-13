import secrets


def generate_state_string(length=16):
    # Generate a secure random string of the specified length
    return secrets.token_urlsafe(length)


# Example usage
state = generate_state_string()
print(state)
