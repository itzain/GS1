from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class ProductBarcodeWizard(models.TransientModel):
    _name = "product.barcode.wizard"

    product_id = fields.Many2one(comodel_name="product.template", string="Product", required=False, )

