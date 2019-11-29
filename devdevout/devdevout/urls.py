from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/',views.about,name='about'),
    url(r'^privacy-policy/',views.privacy,name='privacy'),
    url(r'^affiliate-disclosure/',views.affiliations,name='affiliations'),
    url(r'^$',views.BlogList,name='list'),
    url(r'^posts/(?P<slug>[-\w]+)$',views.BlogDetail,name='detail'),
    url(r'^postsarticle/(?P<slug0>[-\w]+)$',views.BlogDetailArticle,name='detailarticle'),
    url(r'^authorlist/',views.BlogAuthors,name='authorlist'),    
    url(r'^author/(?P<id>\d+)$', views.BlogListByAuthor, name="blog-by-author"),
    url(r'^category/(?P<slug>[-\w]+)/$', views.base, name='category'),
    url(r'^cat/', views.base1, name='cat'),
    url(r'^html-code-examples/', views.html, name='html-code-examples'),
    url(r'^css-code-examples/', views.css, name='css-code-examples'),
    url(r'^javascript-code-examples', views.js, name='javascript-code-examples'),
    url(r'^fashion/', views.fashion, name='fashion'),
    url(r'^finance/', views.finance, name='finance'),
    url(r'^Home_Life/', views.Home_Life, name='Home_Life'),
    url(r'^Technology/', views.Technology, name='Technology'),
    url(r'^Software/', views.Software, name='Software'),

    url(r'^search/',views.search,name='search'),
  

]

