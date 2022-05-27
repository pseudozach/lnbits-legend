from http import HTTPStatus

from fastapi.param_functions import Query
from fastapi.params import Depends
from starlette.exceptions import HTTPException

from lnbits.core.crud import get_user
from lnbits.decorators import WalletTypeInfo, get_key_type

from cktap.verify_link import url_decoder

# from ..satspay.crud import create_charge
from . import satscard_ext
# from .crud import (
#     create_tip,
#     create_satscard,
#     delete_tip,
#     delete_satscard,
#     get_tip,
#     get_satscard,
#     get_satscards,
#     get_tips,
#     update_tip,
#     update_satscard,
# )
# from .helpers import get_charge_details
# from .models import CreateCharge, createTipJar, createTips

@satscard_ext.get("/api/v1/satscard/{data}")
async def api_test_satscard(data: str = Query(None),):
    """Decode satscard url"""
    try:
        # data = 'u=S&o=0&r=2hq9vrvp&n=6b68bc3cbcc33064&s=6d9403679540ea7c5c100bffb013dbcfb7a2c0d59ad8fb972f796fbc5317a01a6be2de10844b66dd3666b8fabd1bf83a95a97ca454c2d542643f411ff16b6802'
        # print('decoding params' + str(data))
        decoded_url = str(url_decoder(data))
        # print('decoded_url ' + decoded_url)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return decoded_url

# @satscard_ext.post("/api/v1/satscard")
# async def api_create_satscard(data: str = Query(None),):
#     """Decode satscard url"""
#     try:
#         # data = 'u=S&o=0&r=2hq9vrvp&n=6b68bc3cbcc33064&s=6d9403679540ea7c5c100bffb013dbcfb7a2c0d59ad8fb972f796fbc5317a01a6be2de10844b66dd3666b8fabd1bf83a95a97ca454c2d542643f411ff16b6802'
#         # print('decoding params' + str(data))
#         decoded_url = str(url_decoder(params))
#         # print('decoded_url ' + decoded_url)
#     except Exception as e:
#         raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

#     return decoded_url

# @satscard_ext.post("/api/v1/satscards")
# async def api_create_satscard(data: createTipJar):
#     """Create a satscard, which holds data about how/where to post tips"""
#     try:
#         satscard = await create_satscard(data)
#     except Exception as e:
#         raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

#     return satscard.dict()


# async def user_from_wallet(wallet: WalletTypeInfo = Depends(get_key_type)):
#     return wallet.wallet.user


# @satscard_ext.post("/api/v1/tips")
# async def api_create_tip(data: createTips):
#     """Take data from tip form and return satspay charge"""
#     sats = data.sats
#     message = data.message
#     if not message:
#         message = "No message"
#     satscard_id = data.satscard
#     satscard = await get_satscard(satscard_id)

#     webhook = satscard.webhook
#     charge_details = await get_charge_details(satscard.id)
#     name = data.name
#     # Ensure that description string can be split reliably
#     name = name.replace('"', "''")
#     if not name:
#         name = "Anonymous"
#     description = f'"{name}": {message}'
#     charge = await create_charge(
#         user=charge_details["user"],
#         data=CreateCharge(
#             amount=sats,
#             webhook=webhook,
#             description=description,
#             onchainwallet=charge_details["onchainwallet"],
#             lnbitswallet=charge_details["lnbitswallet"],
#             completelink=charge_details["completelink"],
#             completelinktext=charge_details["completelinktext"],
#             time=charge_details["time"],
#         ),
#     )

#     await create_tip(
#         id=charge.id,
#         wallet=satscard.wallet,
#         message=message,
#         name=name,
#         sats=data.sats,
#         satscard=data.satscard,
#     )

#     return {"redirect_url": f"/satspay/{charge.id}"}


# @satscard_ext.get("/api/v1/satscards")
# async def api_get_satscards(wallet: WalletTypeInfo = Depends(get_key_type)):
#     """Return list of all satscards assigned to wallet with given invoice key"""
#     wallet_ids = (await get_user(wallet.wallet.user)).wallet_ids
#     satscards = []
#     for wallet_id in wallet_ids:
#         new_satscards = await get_satscards(wallet_id)
#         satscards += new_satscards if new_satscards else []
#     return [satscard.dict() for satscard in satscards] if satscards else []


# @satscard_ext.get("/api/v1/tips")
# async def api_get_tips(wallet: WalletTypeInfo = Depends(get_key_type)):
#     """Return list of all tips assigned to wallet with given invoice key"""
#     wallet_ids = (await get_user(wallet.wallet.user)).wallet_ids
#     tips = []
#     for wallet_id in wallet_ids:
#         new_tips = await get_tips(wallet_id)
#         tips += new_tips if new_tips else []
#     return [tip.dict() for tip in tips] if tips else []


# @satscard_ext.put("/api/v1/tips/{tip_id}")
# async def api_update_tip(
#     wallet: WalletTypeInfo = Depends(get_key_type), tip_id: str = Query(None)
# ):
#     """Update a tip with the data given in the request"""
#     if tip_id:
#         tip = await get_tip(tip_id)

#         if not tip:
#             raise HTTPException(
#                 status_code=HTTPStatus.NOT_FOUND, detail="Tip does not exist."
#             )

#         if tip.wallet != wallet.wallet.id:

#             raise HTTPException(
#                 status_code=HTTPStatus.FORBIDDEN, detail="Not your tip."
#             )

#         tip = await update_tip(tip_id, **g.data)
#     else:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST, detail="No tip ID specified"
#         )
#     return tip.dict()


# @satscard_ext.put("/api/v1/satscards/{satscard_id}")
# async def api_update_satscard(
#     wallet: WalletTypeInfo = Depends(get_key_type), satscard_id: str = Query(None)
# ):
#     """Update a satscard with the data given in the request"""
#     if satscard_id:
#         satscard = await get_satscard(satscard_id)

#         if not satscard:
#             raise HTTPException(
#                 status_code=HTTPStatus.NOT_FOUND, detail="TipJar does not exist."
#             )

#         if satscard.wallet != wallet.wallet.id:
#             raise HTTPException(
#                 status_code=HTTPStatus.FORBIDDEN, detail="Not your satscard."
#             )

#         satscard = await update_satscard(satscard_id, **data)
#     else:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST, detail="No satscard ID specified"
#         )
#     return satscard.dict()


# @satscard_ext.delete("/api/v1/tips/{tip_id}")
# async def api_delete_tip(
#     wallet: WalletTypeInfo = Depends(get_key_type), tip_id: str = Query(None)
# ):
#     """Delete the tip with the given tip_id"""
#     tip = await get_tip(tip_id)
#     if not tip:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND, detail="No tip with this ID!"
#         )
#     if tip.wallet != wallet.wallet.id:
#         raise HTTPException(
#             status_code=HTTPStatus.FORBIDDEN,
#             detail="Not authorized to delete this tip!",
#         )
#     await delete_tip(tip_id)

#     return "", HTTPStatus.NO_CONTENT


# @satscard_ext.delete("/api/v1/satscards/{satscard_id}")
# async def api_delete_satscard(
#     wallet: WalletTypeInfo = Depends(get_key_type), satscard_id: str = Query(None)
# ):
#     """Delete the satscard with the given satscard_id"""
#     satscard = await get_satscard(satscard_id)
#     if not satscard:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND, detail="No satscard with this ID!"
#         )
#     if satscard.wallet != wallet.wallet.id:

#         raise HTTPException(
#             status_code=HTTPStatus.FORBIDDEN,
#             detail="Not authorized to delete this satscard!",
#         )
#     await delete_satscard(satscard_id)

#     return "", HTTPStatus.NO_CONTENT
