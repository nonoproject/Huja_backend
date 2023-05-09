from odoo import models,fields,api
class DoctorServices(models.Model):
    _name = "huja.doctor.services"
    _description= " Describe doctor.service desceription"
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')
    name = fields.Char('Name')
    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True, copy=False,)
    person_id = fields.Many2one('res.users', 'Person')
    department = fields.Char('Department')
    city = fields.Many2one('huja.city', 'City')
    amount = fields.Selection([('free', 'free'),('0-20,000', '0-20,000')], string='Amount')
    phone = fields.Char('Phone')