from django.shortcuts import render, get_object_or_404
from django.db.models import Count
# Create your views here.
from django.http import HttpResponse
from .models import Post,Category
import markdown
from comments.forms import CommentForm
def index(request):
    '''
    #return HttpResponse("欢迎访问我的博客首页！")
    return render(request, 'blog/index.html', context={
                      'title': '我的博客首页', 
                      'welcome': '欢迎访问我的博客首页'
                  })#调用 Django 提供的 render 函数。这个函数根据我们传入的参数来构造 HttpResponse
    #我们首先把 HTTP 请求传了进去，然后 render 根据第二个参数的值 blog/index.html 找到这个模板文件并读取模板中的内容。
    #之后 render 根据我们传入的 context 参数的值把模板中的变量替换为我们传递的变量的值，
    #{{ title }} 被替换成了 context 字典中 title 对应的值，同理 {{ welcome }} 也被替换成相应的值。
    '''
    
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})
    #all 方法返回的是一个 QuerySet（可以理解成一个类似于列表的数据结构）
    #我们紧接着调用了 order_by 方法对这个返回的 queryset 进行排序。
    #排序依据的字段是 created_time，即文章的创建时间。- 号表示逆序，如果不加 - 则是正序
def detail(request,post_pk):
    
    post1=Post.objects.annotate(comment_num=Count('comment'))####注意理解！！！！！！！！！！！！！！！！！！！！！！！！
    post = get_object_or_404(post1, pk=post_pk)###注意理解！！！！！！！！！！！！！
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()
    

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)
#注意这里我们用到了从 django.shortcuts 模块导入的 get_object_or_404 方法，
#其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    

#在模板中找到展示博客文章主体的 {{ post.body }} 部分，为其加上 safe 过滤器，{{ post.body|safe }}，大功告成，这下看到预期效果了。
#safe 是 Django 模板系统中的过滤器（Filter），可以简单地把它看成是一种函数，其作用是作用于模板变量，将模板变量的值变为经过滤器处理过后的值。
#例如这里 {{ post.body|safe }}，本来 {{ post.body }} 经模板系统渲染后应该显示 body 本身的值，但是在后面加上 safe 过滤器后，
#渲染的值不再是body 本身的值，而是由 safe 函数处理后返回的值。过滤器的用法是在模板变量后加一个 | 管道符号，再加上过滤器的名称。
#可以连续使用多个过滤器，例如 {{ var|filter1|filter2 }}。
def archives(request, year, month):#这个是归档的视图链接
    post_list = Post.objects.filter(created_time__year=year,#过滤filter
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request,category_pk):
    cate=get_object_or_404(Category,pk=category_pk)
    post_list=Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})
