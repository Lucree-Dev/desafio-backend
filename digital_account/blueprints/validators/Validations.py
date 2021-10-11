def validate_user_creation(json_data):
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


def validate_card(json_data):
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


def validate_account_transfer(json_data):
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