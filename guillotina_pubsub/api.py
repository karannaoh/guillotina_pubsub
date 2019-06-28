from aiohttp import web
from guillotina import configure
from guillotina.interfaces import IContainer
from guillotina.api.service import Service
# from guillotina.transactions import get_tm
# from guillotina.component import get_utility
# from guillotina_chat.utility import IMessageSender

import aiohttp
import logging

logger = logging.getLogger('guillotina_chat')


@configure.service(context=IContainer, method='GET', name='@content-changes',
                   permission='guillotina.AccessContent')
async def ws_conversate(context, request):
    ws = web.WebSocketResponse()
    # utility = get_utility(IMessageSender)
    # utility.register_ws(ws, request)

    # tm = get_tm()
    # await tm.abort(request)
    # await ws.prepare(request)

    # async for msg in ws:
    #     if msg.tp == aiohttp.WSMsgType.text:
    #         # ws does not receive any messages, just sends
    #         pass
    #     elif msg.tp == aiohttp.WSMsgType.error:
    #         logger.debug('ws connection closed with exception {0:s}'
    #                      .format(ws.exception()))

    # logger.debug('websocket connection closed')
    # utility.unregister_ws(ws)

    return {}