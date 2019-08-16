# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class DocumentShare(models.Model):
    _inherit = 'documents.share'

    security_type = fields.Selection([
        ('none', "None"),
        ('users', "Required Users"),
        ('password', "Password"),
    ], default='none', string="Security type")
    security_user_ids = fields.Many2many('res.users', string='Required Users')
    security_password = fields.Char(string="Password")
