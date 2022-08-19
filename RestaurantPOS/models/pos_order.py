import json

from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)


class POSOrderProduct(models.Model):
    _name ="pos.order.product"

    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)], required=True,
                                 change_default=True)

    qty = fields.Float('Quantity', digits='Product Unit of Measure', default=1)
    price_subtotal = fields.Float(string='Subtotal w/o Tax', digits=0,
                                  readonly=True, required=True)
    price_subtotal_incl = fields.Float(string='Subtotal', digits=0,
                                       readonly=True, required=True)
    total_cost = fields.Float(string='Total cost', digits='Product Price', readonly=True)
    discount = fields.Float(string='Discount (%)', digits=0, default=0.0)
    pos_order_line = fields.Many2one('pos.order.line')

class PosOrderLine(models.Model):
    _inherit = "pos.order.line"


    def create(self,values):
        rec = super(PosOrderLine, self).create(values)
        for line in rec:
            self.env['pos.order.product'].create(
                {'product_id': line.product_id.id,
                    'qty': line.qty,
                    'price_subtotal': line.price_subtotal,
                    'price_subtotal_incl': line.price_subtotal_incl,
                    'total_cost': line.total_cost,
                    'discount': line.discount,
                    'pos_order_line': line.id})
        return rec

    def write(self, values):
        rec = super().write(values)

        pos_order_product=self.env['pos.order.product'].search([('product_id','=',self.product_id.id),
                                              ('pos_order_line', '=', self.ids[0]),
                                              ])
        pos_order_product.write({'qty':self.qty,
                                 'price_subtotal':self.price_subtotal,
                                 'price_subtotal_incl':self.price_subtotal_incl,
                                 'total_cost':self.total_cost,
                                 'discount':self.discount})
        return rec



