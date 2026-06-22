# canary_config.py
# This file controls canary release settings

CANARY_ENABLED = True
CANARY_PERCENTAGE = 10  # 10% of users get new version

STABLE_VERSION = "1.0.0"
CANARY_VERSION = "1.1.0"

def get_version(user_id: int) -> str:
    """
    ELI5: If user_id ends in 0 (10% of users)
    they get canary version, rest get stable.
    """
    if CANARY_ENABLED and (user_id % 10 == 0):
        return CANARY_VERSION
    return STABLE_VERSION
