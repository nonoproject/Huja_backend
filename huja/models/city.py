# -*- coding: utf-8 -*-

from odoo import models, fields, api


class City(models.Model):
    _name = 'huja.city'
    _description = 'Describe city info'

    name = fields.Char('Name')
    phone = fields.Char('Phone')

    area_line = fields.One2many(
        comodel_name='huja.city.area',
        inverse_name='city_id',
        string='Area',
        )


class Area(models.Model):
    _name = 'huja.city.area'
    _description = 'Describe Area info'

    name = fields.Char('Name')
    phone = fields.Char('Phone')
    city_id = fields.Many2one('huja.city')


