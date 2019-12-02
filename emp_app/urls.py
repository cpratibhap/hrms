from rest_framework.routers import SimpleRouter
from .views import StateOperations

simpleRouter = SimpleRouter()

simpleRouter.register('state', StateOperations)

urlpatterns = simpleRouter.urls

