from odoo import fields, models, api

class Medicine(models.Model):
    _name = 'huja.medicine.services'
    _description = 'Describe huja medicine info'
    name = fields.Char('Name')
    phone = fields.Char('Phone')
    city = fields.Many2one('huja.city','City')
    quantity = fields.Selection([('0-5', '6-10')], string='Quantity')
    service_type = fields.Selection([('Available', 'Require')], string='Service Type')
    amount = fields.Selection([('0', '5')], string='Amount')
    date = fields.Date('Date')


