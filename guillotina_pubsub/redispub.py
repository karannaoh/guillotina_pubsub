from guillotina import app_settings
from guillotina import configure
from guillotina.profile import profilable
from guillotina_rediscache import cache
from guillotina_rediscache import serialize
from guillotina_rediscache.interfaces import IRedisChannelUtility

import aioredis
import asyncio
import logging
import pickle

@configure.utility(provides=IRedisChannelUtility)
class Redispub:

    def __init__(self, settings=None, loop=None):
        self._conn = None
        self._loop = loop
        self._settings = {}
        self._ignored_tids = []
        self._pool = None
        self._redis = None
    async def get_conn(self):
        if self._conn is None:
            self._conn = await cache.get_redis_pool(self._loop)
        return self._conn

    async def get_redis(self):
        if self._redis is None:
            self._redis = aioredis.Redis(await self.get_conn())
        return self._redis