# -*- coding: utf-8 -*-
from AptUrl.Helpers import _

from odoo import http
from odoo.http import request, route


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


            # +++++++++++++++++++++++ Create User Api +++++++++++++++++++++++
            # http.request.env['res.users'].create({
            #     'name': 'Omer',
            #     'login': '123',
            #     'password': '111',
            # })

    # Create Home Services

    # Update Home Services
    # Get My Home Services