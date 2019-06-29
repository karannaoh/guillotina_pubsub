from guillotina import configure
from guillotina.interfaces import (IResource, IObjectModifiedEvent)
from guillotina.component import get_utility


@configure.subscriber(for_=(IResource, IObjectModifiedEvent))
async def objectModify(user, event):
    print(user)
    print("dwadawdwadndwadawdja")
    print(event)
