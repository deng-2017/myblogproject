# -*- coding: utf-8 -*-

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

'''
表单是用来收集并向服务器提交用户输入的数据的。考虑用户在我们博客网站上发表评论的过程。当用户想要发表评论时，
他找到我们给他展示的一个评论表单（我们已经看到在文章详情页的底部就有一个评论表单，你将看到表单呈现给我们的样子），
然后根据表单的要求填写相应的数据。之后用户点击评论按钮，这些数据就会发送给某个 URL。
我们知道每一个 URL 对应着一个 Django 的视图函数，于是 Django 调用这个视图函数，
我们在视图函数中写上处理用户通过表单提交上来的数据的代码，比如验证数据的合法性并且保存数据到数据库中，
那么用户的评论就被 Django 后台处理了。如果通过表单提交的数据存在错误，那么我们把错误信息返回给用户，并在前端重新渲染，
并要求用户根据错误信息修正表单中不符合格式的数据，再重新提交。

要使用 Django 的表单功能，我们首先导入 forms 模块。Django 的表单类必须继承自 forms.Form 类或者 forms.ModelForm 类。
如果表单对应有一个数据库模型（例如这里的评论表单对应着评论模型），那么使用 ModelForm 类会简单很多，这是 Django 为我们提供的方便。
之后我们在表单的内部类 Meta 里指定一些和表单相关的东西。model = Comment 表明这个表单对应的数据库模型是 Comment 类。
fields = ['name', 'email', 'url', 'text'] 指定了表单需要显示的字段，这里我们指定了 name、email、url、text 需要显示。
'''