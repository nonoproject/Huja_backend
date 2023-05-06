from odoo import fields, models, api
class phone_balance_services(models.Model):
    _name="huja.phone.balance.services"
    _description="phone balance services description ingo"
    sms_type = fields.Selection([('Sudani','Sudani'),('MTN', 'MTN'),('ZAIN', 'ZAIN')], string='SMS Type')
    description = fields.Text('Description')
    amount = fields.Selection([('0', '500')], string='Amount')
    phone = fields.Char('Phone')