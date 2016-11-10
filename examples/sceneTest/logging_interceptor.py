from src.scene_manager.interceptor.interceptor_I import InterceptorI


class LoggingInterceptor(InterceptorI):

    def update(self, context):
        # log some data
        print "[LOGGING]", context.event.type, context.event.data
