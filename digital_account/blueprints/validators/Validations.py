def validate_user_creation(json_data: dict) -> bool:
    """
    That method will validate all informations receive in the json.
    :param json_data: A dict with information received in the body of json in the post.
    :return: It will return a bool, if all information are in the body of message, it return true, if a specific
             information is not sent, it will return a false.
    """

    if "first_name" not in json_data:
        return False

    if "last_name" not in json_data:
        return False

    if "birthday" not in json_data:
        return False

    if "username" not in json_data:
        return False

    if "password" not in json_data:
        return False

    return True


def validate_card(json_data: dict) -> bool:
    """
    That method will validate all informations receive in the json.
    :param json_data: A dict with information received in the body of json in the post.
    :return: It will return a bool, if all information are in the body of message, it return true, if a specific
             information is not sent, it will return a false.
    """

    if "user_id" not in json_data:
        return False

    if "title" not in json_data:
        return False

    if "pan" not in json_data:
        return False

    if "expiry_mm" not in json_data:
        return False

    if "expiry_yyyy" not in json_data:
        return False

    if "security_code" not in json_data:
        return False

    if "date" not in json_data:
        return False

    return True


def validate_account_transfer(json_data: dict) -> bool:
    """
    That method will validate all informations receive in the json.
    :param json_data: A dict with information received in the body of json in the post.
    :return: It will return a bool, if all information are in the body of message, it return true, if a specific
             information is not sent, it will return a false.
    """

    if "user_id" not in json_data:
        return False

    if "friend_id" not in json_data:
        return False

    if "total_to_transfer" not in json_data:
        return False

    if "billing_card" not in json_data:
        return False

    if "card_id" not in json_data["billing_card"]:
        return False

    return True