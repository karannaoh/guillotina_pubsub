from guillotina import configure
from guillotina import app_settings
from guillotina.interfaces import (IResource, IObjectModifiedEvent)
from guillotina.component import get_utility
from guillotina.interfaces import IPubSubUtility

import json

@configure.subscriber(for_=(IResource, IObjectModifiedEvent))
async def objectModify(user, event):
    print(app_settings)
    print(user)
    util = get_utility(IPubSubUtility)
    await util.publish("test_channel","process",json.dumps({'id': "obj.id",'uuid': "obj.__uuid__",'title': "obj.title"}))
    print(event)
