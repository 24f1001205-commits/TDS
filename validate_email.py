import json
import re

def validate_email(email):
    """
    Validates an email address using a regular expression.
    """
    # A simple regex for email validation
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def main():
    """
    Reads an email from email.json, validates it, and writes the result to a file.
    """
    try:
        with open('email.json', 'r') as f:
            data = json.load(f)
            email = data.get('email', '')

        is_valid = validate_email(email)

        with open('validation_result.txt', 'w') as f:
            if is_valid:
                f.write('Valid')
            else:
                f.write('Invalid')
    except FileNotFoundError:
        with open('validation_result.txt', 'w') as f:
            f.write('Error: email.json not found.')
    except json.JSONDecodeError:
        with open('validation_result.txt', 'w') as f:
            f.write('Error: Could not decode JSON from email.json.')

if __name__ == '__main__':
    main()
