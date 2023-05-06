# -*- coding: utf-8 -*-
# from odoo import http


# class Huja(http.Controller):
#     @http.route('/huja/huja/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/huja/huja/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('huja.listing', {
#             'root': '/huja/huja',
#             'objects': http.request.env['huja.huja'].search([]),
#         })

#     @http.route('/huja/huja/objects/<model("huja.huja"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('huja.object', {
#             'object': obj
#         })
