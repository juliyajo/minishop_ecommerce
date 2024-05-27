from . views import *

def cat(request):
    obj = cate.objects.all()
    return {'c':obj}