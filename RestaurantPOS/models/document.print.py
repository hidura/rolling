import json
from odoo import api, fields, models
import requests

class PrinterDocument(models.Model):

    _name = "document.print"

    docname = fields.Char("DocName")
    data = fields.Char("data")
    is_printed = fields.Boolean("is_printed")
    printer = fields.Char("Printer")



class PrinterPOS(models.Model):
    _name = "document.print.pos"

    printer = fields.Many2one("document.print")
    pos_config = fields.Many2one("pos.config")

