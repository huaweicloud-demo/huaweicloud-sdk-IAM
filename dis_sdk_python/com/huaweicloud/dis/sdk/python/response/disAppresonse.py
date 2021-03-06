#!/usr/bin/python
# -*- coding:utf-8 -*-

from dis_sdk_python.com.huaweicloud.dis.sdk.python.response.disresponse import DisResponse

class disCreateAppResponse(DisResponse):
    def __init__(self, status_code, body):
        DisResponse.__init__(self, status_code, body)



class disdescribeAppResponse(DisResponse):
    def __init__(self, status_code, body):
        DisResponse.__init__(self, status_code, body)


#
# class disApplistResponse(DisResponse):
#     def __init__(self, status_code, body, total_number):
#         app_list = []
#         if 'apps' in body.keys():
#             for i in body.get('apps'):
#                 app_list.append(i.get('app_name'))
#             body.setdefault('apps_list', app_list)
#             body.setdefault('total_number', total_number)
#
#             import copy
#             new_body = copy.deepcopy(body)
#             if 'apps' in new_body.keys():
#                 del new_body['apps']
#             if 'hasMoreApp' in new_body.keys():
#                 del new_body['hasMoreApp']
#
#             new_body.setdefault('appinfo_list', body.get('apps'))
#             new_body.setdefault('has_more_app', body.get('hasMoreApp'))
#
#         else:
#             import copy
#             new_body = copy.deepcopy(body)
#             if 'hasMoreApp' in new_body.keys():
#                 del new_body['hasMoreApp']
#             new_body.setdefault('has_more_app', body.get('hasMoreApp'))
#
#         DisResponse.__init__(self, status_code, new_body)
#         self.body = new_body


class disApplistResponse(DisResponse):
    def __init__(self, status_code, body):
        DisResponse.__init__(self, status_code, body)
        self.has_more_app=body.get('has_more_app','')
        self.apps=body.get('apps','')



class disDeleteAppResponse(DisResponse):
    def __init__(self, status_code, body):
        DisResponse.__init__(self, status_code, body)
