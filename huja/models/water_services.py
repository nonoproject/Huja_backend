from odoo import fields, models, api


class WaterServices(models.Model):
    _name = 'huja.water.services'
    _description = 'Describe Water Services'

    name = fields.Char('Name')
    city = fields.Many2one('huja.city', 'City')
    quantity = fields.Selection([('x', 'X')], string='Quantity')
    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True,
                                     copy=False, )
    Amount = fields.Selection([('x', 'X')], string='Amount')




