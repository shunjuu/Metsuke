from ayumi import Ayumi
from cerberus import Validator
from typing import Dict

_JOB_SCHEMA = {
    "show": {'type': 'string', 'required': True},
    "episode": {'type': 'string', 'required': True},
    "filesize": {'type': 'integer', 'required': True},
    "sub": {'type': 'string', 'required': True}
}
cv = Validator(_JOB_SCHEMA)

def validate(job: Dict) -> bool:
    if cv.validate(job):
        Ayumi.debug("Incoming job validated, returning True.", color=Ayumi.GREEN)
        return True
    else:
        Ayumi.debug("Incoming job is invalid, returning False.", color=Ayumi.YELLOW)
        return False