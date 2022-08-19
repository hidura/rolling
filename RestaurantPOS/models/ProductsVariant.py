import json
from odoo import api, fields, models
import requests


class ProductVariant(models.Model):
    _name = "product.variant"

    variant_name = fields.Char('Variant Name')
    product_id = fields.Many2many("product.product")
    product_target = fields.Many2one("product.product")
    price = fields.Float("Price")


class ProductSuggested(models.Model):
    _name = "product.suggested"

    suggested_name = fields.Char('Suggested Name')
    product_id = fields.Many2one("product.product")
    product_target = fields.Many2many("product.product")
    price = fields.Float("Price")


class ProductOptional(models.Model):
    _name = "product.optionals"

    optionals_name = fields.Char('Optional Name')
    product_target = fields.Many2one("product.product")
    product_id = fields.Many2many("product.product")
    price = fields.Float("Price")



class Terms(models.Model):
    _name = "product.terms"

    term_name = fields.Char('Termino')
    product_id = fields.Many2many("product.product")

#
# class POSSession(models.Model):
#     _inherit = "pos.session"
#     server_id = fields.Integer('Server ID')
#
#     @api.model
#     def create(self, vals):
#         record = super(POSSession, self).create(vals)
#         pos_config = self.env['pos.config'].search([('id', '=', record.config_id.id)])
#         pos_session_info = {'config_id': pos_config.server_id,
#                             "state": 'opened',
#                             "cash_register_id": 1}
#         try:
#             sync_server = self.env['sync.server'].search([])
#             response_load = requests.post('{}/newpossession'.format(sync_server.route),
#                                           data=json.dumps(pos_session_info))
#             self.env['sync.possession'].create({'pos_session': record.id,
#                                                 'response_code': response_load.status_code,
#                                                 'response_content': response_load.content.decode()})
#             if response_load.status_code == 200:
#                 resp_data = json.loads(response_load.content.decode())
#                 record.write({'server_id': resp_data['data']['server_id']})
#         except:
#             self.env['sync.possession'].create({'pos_session': record.id,
#                                                 'response_code': 500,
#                                                 'response_content': "Remote not connected"})
#
#         return record
# class POSORDER(models.Model):
#     _inherit = "pos.order"
#
#     server_id = fields.Integer('Server ID')
#     nif=fields.Char('NIF') #THE NIF NUMBER IS THE NUMBER THAT DELIVER THE FISCAL PRINTER
#
#
#
#
# class POSORDERLine(models.Model):
#     _inherit = "pos.order.line"
#
#     server_id = fields.Integer('Server ID')
#
#
# class POSPayment(models.Model):
#     _inherit = "pos.payment"
#
#     server_id = fields.Integer('Server ID')
#     payment_fiscal = fields.Char('ID PAGO FISCAL')
#
#
#
# class POSPaymentMethod(models.Model):
#     _inherit = "pos.payment.method"
#
#     server_id = fields.Integer('Server ID')
#     payment_fiscal = fields.Char('ID PAGO FISCAL')
#
#
# class LatanDocumentType(models.Model):
#     _inherit = "l10n_latam.document.type"
#
#     document_by_default = fields.Boolean('Document by default to use',default=False)
#
# class ResPartner(models.Model):
#     _inherit = "res.partner"
#
#     server_id = fields.Integer('Server ID')
#
# class FiscalPOS(models.Model):
#     _name = "fiscal.pos"
#     _description = "The fiscal POS is the register of the " \
#                    "connection between the local server and the fiscalapp"
#     server_path = fields.Char('Path Route to the server' )
#     pos_config = fields.Many2one('pos.config')
#     printer_id = fields.Char('Printer ID')
#     printer_serial = fields.Char('Printer Serial')
#     copies = fields.Integer('Copies', default=1)
#
#     pos_fiscal_active = fields.Boolean('POS Fiscal Activo?',default=False)
#
#     @api.model
#     def create(self, vals):
#         response_load = requests.get('{}/printer_information'.format(vals['server_path']))
#         resp = json.loads(response_load.content.decode())
#         posconfig = self.env['pos.config'].search([('id', '=', self.pos_config.id)])
#         if response_load.status_code == 200:
#             vals['printer_serial']=resp['response']['serial']
#             vals['printer_id']=resp['response']['id']
#             posconfig.write({'pos_fiscal':True})
#         else:
#             posconfig.write({'pos_fiscal':False})
#             raise Exception(str("Hubo un problema de comunicacion con el sistema"))
#         record = super(FiscalPOS, self).create(vals)
#
#         return record
#
#     @api.model
#     def write(self, vals):
#         response_load = requests.get('{}/printer_information'.format(vals['server_path']))
#         resp = json.loads(response_load.content.decode())
#         posconfig = self.env['pos.config'].search([('id', '=', self.pos_config.id)])
#         if response_load.status_code == 200:
#             vals['printer_serial'] = resp['response']['serial']
#             vals['printer_id'] = resp['response']['id']
#             posconfig.write({'pos_fiscal': True})
#         else:
#             posconfig.write({'pos_fiscal': False})
#             raise Exception(str("Hubo un problema de comunicacion con el sistema"))
#         record = super(FiscalPOS, self).write(vals)
#
#         return record
#
#
# class FiscalClosePOS(models.Model):
#     _name = "fiscal.monthly.close.pos"
#     _description = "The fiscal close of the month."
#     month = fields.Char('Month in MM')
#     year = fields.Char('Year in YYYY')
#     fiscal_pos = fields.Many2one('fiscal.pos')
#     server_response = fields.Text('Respuesta del servidor')
#
#     @api.model
#     def create(self, vals):
#         response_load = requests.get('{}/monthly_book/{}/{}'.format(self.fiscal_pos.server_path,self.month,self.year), stream=True)
#         if response_load.status_code == 200:
#             path='~/Downloads/LV{}{}.txt'.format(self.month,self.year)
#             with open(path, 'wb') as f:
#                 for chunk in response_load.iter_content(1024):
#                     f.write(chunk)
#         else:
#             self.pos_config.write({'pos_fiscal':False})
#             raise Exception(str("Hubo un problema de comunicacion con el sistema"))
#         record = super(FiscalClosePOS, self).create(vals)
#         return record
#
#
#
#
#
# class SyncServer(models.Model):
#     _name = "sync.server"
#     _description = "This table is to register the syncronization server information the " \
#                    "Port between Odoo local and Odoo remote."
#     route = fields.Char('Route of the main server')
#     name = fields.Char('Nombre del servidor')
#
#
#
# class SyncBill(models.Model):
#     _name = "sync.bill"
#     _description = "This table sync the pos with the system."
#     pos_order = fields.Many2one('pos.order')
#     bill = fields.Many2one('sale.order')
#     save_it = fields.Boolean('Boolean')
#     response_content = fields.Text('Respuesta del servidor')
#     response_code = fields.Text('Respuesta del servidor')
#     bill_type = fields.Selection([( 'regular_bill','Factura Regular'),
#                                   ('pos_bill','Factura Punto de venta')])
#
#
# class SyncPosSession(models.Model):
#     _name = "sync.possession"
#     _description = "This table sync the pos with the system."
#     pos_session = fields.Many2one('pos.session')
#     response_code = fields.Integer('Codigo de respuesta')
#     response_content = fields.Text('Contenido de respuesta')
#
#
#
#
# class AccountMove(models.Model):
#     _inherit = "account.move"
#     server_id = fields.Integer('Server ID')
#
#     @api.model
#     def action_sync_manual_account_move(self, vals):
#
#         sync_server = self.env['sync.server'].search([])
#         response_load = requests.post('{}/account_move_sync'.format(sync_server.route),
#                                       data=json.dumps({'account_move':vals[0]}))
#
#         if response_load.status_code == 200:
#             resp_data = json.loads(response_load.content.decode())
#
#
#
# class AccountMoveLine(models.Model):
#     _inherit = "account.move.line"
#     server_id = fields.Integer('Server ID')
#
# class AccountTax(models.Model):
#     _inherit = "account.tax"
#     server_id = fields.Integer('Server ID')
