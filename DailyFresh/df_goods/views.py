from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-g_click')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-g_click')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-g_click')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-g_click')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-g_click')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-g_click')[0:4]

    context = {'title': '首页',
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type21': type21,
               'type3': type3, 'type31': type31,
               'type4': type4, 'type41': type41,
               'type5': type5, 'type51': type51
               }

    return render(request, 'df_goods/index.html', context)


def detail(request, typeid, goodid):
    news = GoodsInfo.objects.filter(g_type_id=int(typeid)+1)[0:2]
    goods = GoodsInfo.objects.get(id=int(goodid), g_type_id=int(typeid)+1)
    goods.g_click = goods.g_click + 1
    goods.save()
    context = {'goods': goods, 'news': news}

    return render(request, 'df_goods/detail.html', context)


def type_list(request, typeid, pindex, sort):
    list = []
    sort = int(sort)
    typeid = int(typeid)+1
    if sort == 1:
        list = GoodsInfo.objects.filter(g_type_id=typeid)  # 默认
    elif sort == 2:
        list = GoodsInfo.objects.filter(g_type_id=typeid).order_by('-g_price')  # 价格
    elif sort == 3:
        list = GoodsInfo.objects.filter(g_type_id=typeid).order_by('-g_click')  # 人气

    news = GoodsInfo.objects.filter(g_type_id=typeid)[0:2]
    p = Paginator(list, 1)
    pindex = int(pindex)
    page = p.page(int(pindex))
    prange = p.page_range
    print(list)
    print(prange)
    print(pindex)
    typeid = str(typeid - 1)
    context = {'list': list, 'page': page, 'prange': prange, 'pindex': pindex, 'sort': sort, 'typeid': typeid, 'news': news}
    return render(request, 'df_goods/list.html', context)