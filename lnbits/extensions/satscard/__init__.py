from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_satscard")

satscard_ext: APIRouter = APIRouter(prefix="/satscard", tags=["satscard"])


def satscard_renderer():
    return template_renderer(["lnbits/extensions/satscard/templates"])


from .views import *  # noqa
from .views_api import *  # noqa
