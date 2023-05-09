
from odoo import models,fields,api
class ElectricityServices(models.Model):
    _name = "huja.electricity.services"
    _rec_name = 'description'
    _description= " Describe electricity.services desceription"
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')
    description = fields.Char('Description')
    person_id = fields.Many2one('res.users', 'Person')
    electricity_meter_number = fields.Char('Electricity Meter Number')
    services_type = fields.Selection([('available', 'Available'),('required', 'Required')], string='Services Type', required=True, tracking=True, copy=False,)
    amount = fields.Selection([('free', 'free'),('0-20000', '0-20000')], string='Amount')
    quantity = fields.Selection([('05', '05')], string='Quantity')
    phone = fields.Char('Phone')