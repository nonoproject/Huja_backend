from odoo import fields, models, api
class missing_people_services(models.Model):
    _name = 'huja.missing.people.services'
    _description = 'Describe huja missing people info'
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')
    name = fields.Char('Name')
    description = fields.Text('Description')
    phone = fields.Char('Phone')
    city = fields.Many2one('huja.city','City')
    date = fields.Date('Date')
    