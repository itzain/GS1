# -*- coding: utf-8 -*-

from odoo import models, fields, api
from  datetime import datetime

class StockMove(models.Model):
    _inherit='stock.move'

    product_barcode= fields.Char(string="Product Barcode",compute='_calc_product_barcode',store=True)
    global_barcode= fields.Char(string="Gobal Barcode",compute='_calc_product_barcode',store=True)
    serial_no= fields.Char(string="Serial Number",compute='_calc_product_barcode',store=True)
    expiration_date= fields.Date(string="expiration date",compute='_calc_product_barcode',store=True)

# """
# 01
    # 08717872006413
    # 17
    # 260308
    # 102000420002305

# """

    @api.depends('product_id')
    def _calc_product_barcode(self):
        for move in self:
            if move.product_id.barcode:
                try:
                    barcode = move.product_id.barcode
                    year = barcode[18:20]
                    month = barcode[20:22]
                    day = barcode[22:24]
                    expiration_date = datetime(2000+int(year),int(month),int(day))
                    move.product_barcode = barcode
                    move.global_barcode = barcode[2:16]
                    move.expiration_date = expiration_date
                    move.serial_no = barcode[24:]
                except:
                    move.product_barcode = move.product_id.barcode
                    move.global_barcode =""
                    move.serial_no =""
                    move.expiration_date =False

