from ayumi import Ayumi
from cerberus import Validator
from typing import Dict

cv = Validator({
    "show": {'type': 'string', 'required': True},
    "episode": {'type': 'string', 'required': True},
    "filesize": {'type': 'integer', 'required': True},
    "sub": {'type': 'string', 'required': True}
})

fiv = Validator({
    "title": {'type': 'string', 'required': True},
    "link": {'type': 'string', 'required': True},
    "guid": {'type': 'string', 'required': True},
    "show_title": {'type': 'string', 'required': False}
})


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


class FeedItem:

    def __init__(self, title: str = None, link: str = None, guid: str = None, show_title: str = None):
        self._title = title
        self._link = link
        self._guid = guid
        self._show_title = show_title

    @property
    def title(self) -> str:
        return self._title

    @property
    def link(self) -> str:
        return self._link

    @property
    def guid(self) -> str:
        return self._guid
    
    @property
    def show_title(self) -> str:
        return self._show_title

def validate(job: Dict) -> bool:
    """Alias for validate_job, meant to support older versions."""
    return validate_job(job)


def validate_job(job: Dict) -> bool:
    if cv.validate(job):
        Ayumi.debug("Incoming job validated, returning True.",
                    color=Ayumi.GREEN)
        return True
    else:
        Ayumi.debug("Incoming job is invalid, returning False.",
                    color=Ayumi.YELLOW)
        return False


def validate_feeditem(item: Dict) -> bool:
    if fiv.validate(item):
        Ayumi.debug("Incoming feed item validated, returning True.",
                    color=Ayumi.GREEN)
        return True
    else:
        Ayumi.debug("Incoming feed item is invalid, returning False.",
                    color=Ayumi.YELLOW)
        return False


def generate(job: Dict) -> Job:
    return generate_job(job)


def generate_job(job: Dict) -> Job:
    return Job(
        show=job['show'],
        episode=job['episode'],
        filesize=job['filesize'],
        sub=job['sub']
    )


def generate_feeditem(item: Dict) -> FeedItem:
    return FeedItem(
        title=item['title'],
        link=item['link'],
        guid=item['guid'],
        show_title=item['show_title']
    )
