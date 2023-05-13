# -*- coding: utf-8 -*-
from AptUrl.Helpers import _

from odoo import http
from odoo.http import request, route
from datetime import date


class HomeServices(http.Controller):
    # Get All Home
    @route(['/huja/api/services/home/get_all'], type="json", auth="user")
    def get_home_services(self, **kw):
        if request.jsonrequest:
            user_id = request.env.user.id
            home_ids = http.request.env['huja.home.services'].sudo().search([])
            home_list = []
            try:
                if user_id:
                    if home_ids:
                        for home in home_ids:
                            home_list.append({
                                'id': home.id,
                                'name': home.name,
                                'city': home.city.name,
                                'area': home.area.name,
                                'hosting_type': home.hosting_type,
                                'room_number': home.room_number,
                                'people_number': home.people_number,
                                'amount': home.amount,
                                'phone': home.person_id.phone,
                                'date': home.date,
                            })
                        return {"code": 200, "message": _("Successfully"), "data": home_list}
                    else:
                        return {"code": 204, "message": _("No Home"), "data": []}
                else:
                    return {"code": 204, "message": _("No User"), "data": []}
            except Exception as e:
                return {"code": 404, "message": _("Failed to Fetch Home"), "data": e}

    # Create Home Services
    @route(['/huja/api/services/home/create'], type="json", auth="user")
    def create_home_services(self, **kw):
        if request.jsonrequest:
            if kw.get('name') and kw.get('city') and kw.get('area') and kw.get('hosting_type') and kw.get('room_number') \
                    and kw.get('services_type') and kw.get('people_number') and kw.get('amount'):
                user = request.env.user
                try:
                    vals = ({
                        'name': kw['name'],
                        'city': kw['city'],
                        'person_id': user.id,
                        'area': kw['area'],
                        'hosting_type': kw['hosting_type'],
                        'room_number': kw['room_number'],
                        'services_type': kw['services_type'],
                        'people_number': kw['people_number'],
                        'amount': kw['amount'],
                        'date': date.today(),
                    })
                    new_home_service = http.request.env['huja.home.services'].sudo().create(vals)
                    return {"code": 200, "message": _("Successfully"), "data": new_home_service.id}
                except Exception as e:
                    return {"code": 400, "message": _("Failed to Create"), "data": e}
            else:
                return {"code": 404, "message": _("Missing Required Field"), "data": []}
    # Update Home Services
    @route(['/huja/api/services/home/update_my_home_services'], type="json", auth="user")
    def update_my_home_services(self, **kw):
        if request.jsonrequest:
            if kw.get('id') and kw.get('action_type'):
                try:
                    my_home_service = http.request.env['huja.home.services'].sudo().search([('id','=',kw.get('id'))])
                    if my_home_service:
                        if kw.get('action_type') == 'done':
                            my_home_service.action_to_done()
                        else:
                            my_home_service.action_to_cancel()
                        return {"code": 200, "message": _("Successfully"), "data": my_home_service.id}
                    else:
                        return {"code": 404, "message": _("Not Found"), "data": []}
                except Exception as e:
                    return {"code": 400, "message": _("Failed to Create"), "data": e}
            else:
                return {"code": 404, "message": _("Missing Required Field"), "data": []}

    # Get My Home Services
    @route(['/huja/api/services/home/get_my_home_services'], type="json", auth="user")
    def get_my_home_services(self, **kw):
        if request.jsonrequest:
            user_id = request.env.user.id
            home_ids = http.request.env['huja.home.services'].sudo().search([('person_id','=',user_id)])
            home_list = []
            try:
                if user_id:
                    if home_ids:
                        for home in home_ids:
                            home_list.append({
                                'id': home.id,
                                'name': home.name,
                                'city': home.city.name,
                                'area': home.area.name,
                                'hosting_type': home.hosting_type,
                                'room_number': home.room_number,
                                'people_number': home.people_number,
                                'amount': home.amount,
                                'phone': home.person_id.phone,
                                'date': home.date,
                            })
                        return {"code": 200, "message": _("Successfully"), "data": home_list}
                    else:
                        return {"code": 204, "message": _("No Home"), "data": []}
                else:
                    return {"code": 204, "message": _("No User"), "data": []}
            except Exception as e:
                return {"code": 404, "message": _("Failed to Fetch Home"), "data": e}

