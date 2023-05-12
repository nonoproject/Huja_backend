from odoo import fields, models, api


class TripServices(models.Model):
    _name = 'huja.trips.services'
    _description = 'Describe Trip Services'
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')

    name = fields.Char('Name')
    person_id = fields.Many2one('res.users', 'Person')
    from_location = fields.Many2one('huja.city', 'From Location')
    to_location = fields.Many2one('huja.city', 'To Location')
    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True,
                                     copy=False, )
    people_number = fields.Selection([('x', 'X')], string='People Number')
    amount = fields.Selection([('x', 'X')], string='Amount')
    date = fields.Date('Date')


