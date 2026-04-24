# import xadmin
from django.urls import include,re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'xadmin/', include(xadmin.site.urls)),  # xadmin

    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 富文本编辑器

    re_path(r'^', include('verifications.urls')),  # 发短信模块

    re_path(r'^', include('users.urls')),  # 用户模块

    re_path(r'^oauth/', include('oauth.urls')),  # QQ模块

    re_path(r'^', include('areas.urls')),  # 省市区模块

    re_path(r'^', include('goods.urls')),  # 商品模块

    re_path(r'^', include('carts.urls')),  # 购物车模块

    re_path(r'^', include('orders.urls')),  # 订单模块

    re_path(r'^', include('payment.urls')),  # 支付模块
]
