# -*- coding: utf-8 *-*
from selene.web import handlers
from tornado.web import url


urls = [
    url(r"/", handlers.HomeHandler, name='home'),
    url(r"/page/([0-9]+)", handlers.HomeHandler, name='home-page'),
    url(r"/register", handlers.RegisterHandler, name='register'),
    url(r"/login", handlers.LoginHandler, name='login'),
    url(r"/login/google", handlers.LoginGoogleHandler, name='login-google'),
    url(r"/login/twitter/?", handlers.LoginTwitterHandler,
        name='login-twitter'),
    url(r'/confirm-account/(.*)', handlers.ConfirmAccountHandler,
        name='confirm-account'),
    url(r'/new-password', handlers.RequestNewPasswordHandler,
        name='new-password'),
    url(r'/reset-password/(.*)', handlers.ResetPasswordHandler,
        name='reset-password'),
    url(r"/logout", handlers.LogoutHandler, name='logout'),
    url(r'/change-language', handlers.ChangeLanguageHandler,
        name='change-language'),
    url(r'/my-account', handlers.AccountHandler, name='my-account'),
    url(r"/post/new", handlers.NewPostHandler, name='post-new'),
    url(r"/post/([a-zA-Z0-9-]+)", handlers.PostHandler, name='post'),
    url(r"/post/([a-zA-Z0-9-]+)/edit", handlers.EditPostHandler,
        name='post-edit'),
    url(r"/post/([a-zA-Z0-9-]+)/delete", handlers.DeletePostHandler,
        name='post-delete'),
    url(r"/post/([a-zA-Z0-9-]+)/vote", handlers.VotePostHandler,
        name='post-vote'),
    url(r'/posts', handlers.PostsHandlers, name='posts'),
    url(r'/tag/([a-zA-Z0-9-]+)', handlers.TagHandler, name='tag'),
    url(r'/tag/([a-zA-Z0-9-]+)/page/([0-9]+)?', handlers.TagHandler,
        name='tag-page'),
    url(r'/tags', handlers.TagsHandlers, name='tags'),
    url(r'/search', handlers.SearchHandler, name='search'),
    url(r'/post/([a-zA-Z0-9-]+)/comment/new', handlers.NewCommentHandler,
        name='comment-new'),
    url(r'/comment/([a-z0-9]{24})/(like|dislike)', handlers.LikeCommentHandler,
        name='comment-like'),
    url(r'/comment/([a-z0-9]{24})/edit', handlers.EditCommentHandler,
        name='comment-edit'),
    url(r'/comment/([a-z0-9]{24})/delete', handlers.DeleteCommentHandler,
        name='comment-delete'),
    #url(r"/feed.rss", handlers.RSSHandler, name='rss'),
    url(r"/feed.atom", handlers.AtomHandler, name='atom')]
