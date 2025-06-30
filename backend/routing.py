from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import recipes.routing  # 👈 you'll create this next

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            recipes.routing.websocket_urlpatterns
        )
    ),
})
