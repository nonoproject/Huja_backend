from odoo import fields, models, api
class phone_balance_services(models.Model):
    _name="huja.phone.balance.services"
    _rec_name = "description"
    _description="phone balance services description ingo"
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')
    sim_type = fields.Selection([('sudani','Sudani'),('mtn', 'MTN'),('zain', 'ZAIN')], string='Sim Type')
    person_id = fields.Many2one('res.users', 'Person')
    description = fields.Char('Description')
    amount = fields.Selection([('0', '500')], string='Amount')
    phone = fields.Char('Phone')