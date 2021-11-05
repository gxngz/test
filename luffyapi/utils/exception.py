from rest_framework.views import exception_handler
from utils.response import APIResponse
from .logging import logger
def custom_exception_handler(exc, context):
    res = exception_handler(exc,context)
    logger.error("%s---view:发生错误：%s"%(context["view"].__class__.__name__,str(exc)))
    if not res:
        return APIResponse(code=100,msg="error",data=str(exc))
    else:
        return APIResponse(code=100, msg="error",data=res.data)