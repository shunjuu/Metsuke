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

class Job:

    def __init__(self, show: str = None, episode: str = None, filesize: int = -1, sub: str = None):
        self._show = Job._clean(show)
        self._episode = Job._clean(episode)
        self._filesize = filesize
        self._sub = sub.upper()

    @property
    def show(self) -> str:
        return self._show

    @property
    def episode(self) -> str:
        return self._episode

    @property
    def filesize(self) -> int:
        return self._filesize

    @property
    def sub(self) -> str:
        return self._sub

    @staticmethod
    def _clean(name: str) -> str:
        if name.endswith("/"):
            return name[:-1]
        else:
            return name

def validate(job: Dict) -> bool:
    if cv.validate(job):
        Ayumi.debug("Incoming job validated, returning True.", color=Ayumi.GREEN)
        return True
    else:
        Ayumi.debug("Incoming job is invalid, returning False.", color=Ayumi.YELLOW)
        return False

def generate(job: Dict) -> Job:
    return Job(
        show=job['show'],
        episode=job['episode'],
        filesize=job['filesize'],
        sub=job['sub']
    )