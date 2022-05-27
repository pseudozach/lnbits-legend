from http import HTTPStatus

from fastapi import Request
from fastapi.param_functions import Query
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException

from lnbits.core.models import User
from lnbits.decorators import check_user_exists

from . import satscard_ext, satscard_renderer
# from .crud import get_tipjar

templates = Jinja2Templates(directory="templates")


@satscard_ext.get("/")
async def index(request: Request, user: User = Depends(check_user_exists)):
    return satscard_renderer().TemplateResponse(
        "satscard/index.html", {"request": request, "user": user.dict()}
    )


# @satscard_ext.get("/{satscard_id}")
# async def tip(request: Request, tipjar_id: int = Query(None)):
#     """Return the donation form for the Tipjar corresponding to id"""
#     tipjar = await get_tipjar(tipjar_id)
#     if not tipjar:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND, detail="TipJar does not exist."
#         )

#     return tipjar_renderer().TemplateResponse(
#         "tipjar/display.html",
#         {"request": request, "donatee": tipjar.name, "tipjar": tipjar.id},
#     )
