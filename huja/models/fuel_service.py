from odoo import models,fields,api
class FuelServices(models.Model):

    _name = "huja.fuel.services"
    _rec_name = "fuel_type"
    _description= " Describe fuel.services desceription"

    def action_to_done(self):
        self.status = "done"
    def action_to_cancel(self):
        self.status = "ancel"

    services_type = fields.Selection([('available', 'Available'),
                                      ('required', 'Required')], string='Services Type', required=True, tracking=True, copy=False,)
    fuel_type = fields.Selection([('Gaz', 'Gaz'),
                                      ('Benzine', 'Benzine')], string='Fuel Type', required=True)
    quantity = fields.Selection([('0-5', '6-10')], string='Quantity')
    city = fields.Many2one('huja.city', 'City')
    amount = fields.Selection([('free', 'free'),('0-20,000', '0-20,000')], string='Amount')
    phone = fields.Char('Phone')
    status = fields.Selection([('draft','Draft'),('done', 'Done'),('cancel', 'Cancel')],default = 'Draft', string='Status')

