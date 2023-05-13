from AptUrl.Helpers import _

from odoo import http
from odoo.http import request, route


class HujaAuthentication(http.Controller):

    @route(['/huja/api/authentication/register'], type="json", auth="public")
    def huja_register(self, **kw):
        if request.jsonrequest:
            if kw.get('name') and kw.get('phone'):
                try:
                    check_user = http.request.env['res.users'].search([('login', '=', kw.get('phone'))])
                    if not check_user:
                        http.request.env['res.users'].create({
                            'name': kw.get('name'),
                            'login': kw.get('phone'),
                            'password': kw.get('phone'),
                            'phone': kw.get('phone'),
                        })
                        return {"code": 200, "message": _("Register Successfully "), "data": []}
                    else:
                        return {"code": 404, "message": _("The User Already Exists "), "data": []}
                except Exception as e:
                    return {"code": 400, "message": _("Failed to Register"), "data": e}
            else:
                return {"code": 404, "message": _("Missing Required Field"), "data": []}
