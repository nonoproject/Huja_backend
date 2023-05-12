from odoo import fields, models, api


class WaterServices(models.Model):
    _name = 'huja.water.services'
    _description = 'Describe Water Services'
    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "cancel"
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'draft', string='Status')

    name = fields.Char('Name')
    person_id = fields.Many2one('res.users', 'Person')
    city = fields.Many2one('huja.city', 'City')
    quantity = fields.Selection([('x', 'X')], string='Quantity')
    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True,
                                     copy=False, )
    amount = fields.Selection([('x', 'X')], string='Amount')




# access_electricity_service,huja.electricity.services,model_huja_electricity_services,,1,1,1,1
# access_fuel_service,huja.fuel.services,model_huja_fuel_services,,1,1,1,1
#