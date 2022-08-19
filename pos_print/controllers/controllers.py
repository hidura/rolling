# -*- coding: utf-8 -*-
# from odoo import http


# class PosPrint(http.Controller):
#     @http.route('/pos_print/pos_print', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_print/pos_print/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_print.listing', {
#             'root': '/pos_print/pos_print',
#             'objects': http.request.env['pos_print.pos_print'].search([]),
#         })

#     @http.route('/pos_print/pos_print/objects/<model("pos_print.pos_print"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_print.object', {
#             'object': obj
#         })
