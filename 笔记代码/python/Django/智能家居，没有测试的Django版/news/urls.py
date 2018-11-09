"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import view,Mysqldb,Web_get,Web_post,customer,udpserver
import thread
import threading
import logging_set.log_message
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello$', view.hello),
    url(r'^testdb$', Mysqldb.testdb),
    url(r'^Online$', customer.Online),
    url(r'^Control_mac$', customer.Control_mac),
    url(r'^Control_switch$', customer.Control_switch),
    # url(r'^search-form$', search.search_form),
    # url(r'^search$', search.search),
    # url(r'^search-post$', search2.search_post),
]
# if __name__ == "__main__":
#     try:
#         threading.Thread(target=udpserver.startservice).start()   
#     except:
#         logging_set.log_message.logging.warning('fail to create threads')