from odoo import fields, models, api


class TripServices(models.Model):
    _name = 'huja.trips.services'
    _description = 'Describe Trip Services'

    name = fields.Char('Name')
    from_location = fields.Many2one('huja.city', 'From Location')
    to_location = fields.Many2one('huja.city', 'To Location')
    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True,
                                     copy=False, )
    people_number = fields.Selection([('x', 'X')], string='People Number')
    Amount = fields.Selection([('x', 'X')], string='Amount')
    date = fields.Date('Date')


