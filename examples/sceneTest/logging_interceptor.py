from src.scene_manager.interceptor.interceptor_I import Interceptor


class LoggingInterceptor(Interceptor):

    def update(self, context):
        # log some data
        print "[LOGGING]", context.event.type, context.event.data
