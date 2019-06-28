from guillotina import configure
from guillotina.interfaces import (IResource, IObjectModifiedEvent)


@configure.subscriber(for_=(IResource, IObjectModifiedEvent))
async def objectModify(user, event):
    print("userdwajdbwiabdiawbdiawdijwad")
    print(user)
    print("eventdwaidbawidawidba")
    print(event)
