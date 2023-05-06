from odoo import fields, models, api


class HomeServices(models.Model):
    _name = 'huja.home.services'
    _description = 'Describe home services'
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')
    name = fields.Char('Name')
    city = fields.Many2one('huja.city', 'City')
    area = fields.Many2one('huja.city.area', 'Area')
    hosting_type = fields.Selection([('family', 'Family'),
                                     ('individual', 'Individual')], string='Hosting Type', required=True, tracking=True, copy=False,)
    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True, copy=False,)
    room_number = fields.Selection([('x', 'X')], string='Room Number')
    people_number = fields.Selection([('x', 'X')], string='People Number')
    Amount = fields.Selection([('x', 'X')], string='Amount')
    date = fields.Date('Date')


