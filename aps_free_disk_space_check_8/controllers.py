# -*- coding: utf-8 -*-
from openerp import http

# class ApsFreeDiskSpaceCheck8.0(http.Controller):
#     @http.route('/aps_free_disk_space_check_8.0/aps_free_disk_space_check_8.0/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aps_free_disk_space_check_8.0/aps_free_disk_space_check_8.0/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aps_free_disk_space_check_8.0.listing', {
#             'root': '/aps_free_disk_space_check_8.0/aps_free_disk_space_check_8.0',
#             'objects': http.request.env['aps_free_disk_space_check_8.0.aps_free_disk_space_check_8.0'].search([]),
#         })

#     @http.route('/aps_free_disk_space_check_8.0/aps_free_disk_space_check_8.0/objects/<model("aps_free_disk_space_check_8.0.aps_free_disk_space_check_8.0"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aps_free_disk_space_check_8.0.object', {
#             'object': obj
#         })