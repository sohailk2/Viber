# from django.conf import settings

# class Routers(object):
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'genre':
#             return 'genredb'
#         if model._meta.app_label == 'tracks':
#             return 'tracksdb'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'genre':
#             return 'genredb'
#         if model._meta.app_label == 'tracks':
#             return 'tracksdb'
#         return 'default'
    
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Do not allow migrations on the remote database
#         """
#         if app_label == 'genre' or app_label == 'tracks' or app_label == 'default':
#             return True
#         return True

