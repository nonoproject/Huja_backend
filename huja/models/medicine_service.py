from odoo import fields, models, api

class Medicine(models.Model):
    _name = 'huja.medicine.services'
    _description = 'Describe huja medicine info'
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')
    name = fields.Char('Name')
    person_id = fields.Many2one('res.users', 'Person')
    phone = fields.Char('Phone')
    city = fields.Many2one('huja.city','City')
    quantity = fields.Selection([('0-5', '6-10')], string='Quantity')
    service_type = fields.Selection([('Available', 'Require')], string='Service Type')
    amount = fields.Selection([('0', '5')], string='Amount')
    date = fields.Date('Date')


