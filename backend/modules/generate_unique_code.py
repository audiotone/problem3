import uuid

def generate_unique_code():
    """
    Function to generate a random unique code
    :return:
    """
    unique_code = str(uuid.uuid4())
    return unique_code
