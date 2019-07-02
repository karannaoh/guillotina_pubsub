from aiohttp import web
from guillotina import configure
from guillotina.interfaces import IResource
from guillotina.api.service import Service
# from guillotina.transactions import get_tm
# from guillotina.component import get_utility
# from guillotina_chat.utility import IMessageSender

import aiohttp
import logging

logger = logging.getLogger('guillotina_chat')


@configure.service(context=IResource, method='GET', name='@content-changes',
                   permission='guillotina.AccessContent')
async def ws_conversate(context, request):
    ws = web.WebSocketResponse()

    return {}