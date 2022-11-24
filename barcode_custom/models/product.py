from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError, ValidationError

class ProductSerial(models.Model):
    _inherit = 'product.template'

    global_barcode = fields.Char(string="Global Barcode", store=True,readonly=False)

    def  calc_global_barcode(self):
        for rec in self:
            if rec.barcode:
                stander = rec.barcode[0:2]
                print('standerrr',stander)
                if stander == '01':
                    print('AAAAAAAAAAAAAAAa')
                    rec.barcode = rec.barcode[2:16]
                else:
                    raise ValidationError(_('Global Barcode Not Valid !'))
            else:
                rec.barcode = False



class StockSerials(models.Model):
    _inherit = 'stock.move.line'

    barcode = fields.Char(string="Barcode", store=True,readonly=False)
    global_barcode = fields.Char(string="Global Barcode",compute='_calc_product_barcode', store=True,readonly=False)
    expiration_dates= fields.Date(string="expiration date", store=True, readonly=False)
    barcode_date = fields.Char(string="Expiration Date Number",compute='_calc_product_barcode', store=True, readonly=False)
    batch_no = fields.Char(string="Batch Number \ Lot",compute='_calc_product_barcode', store=True,readonly=False)
    serial_no = fields.Char(string="Serial Number",compute='_calc_product_barcode',  store=True,readonly=False)
    # qty_done = fields.Float('Done', default=1, digits='Product Unit of Measure', copy=False)

    @api.depends('barcode')
    def _calc_product_barcode(self):
        for rec in self:
            if rec.barcode:

                barcode = rec.barcode
                start_expiration_date = barcode[17:18]
                year = barcode[18:20]
                month = barcode[20:22]
                day = barcode[22:24]
                barcode_date_num = barcode[18:24]
                if year and month and day:
                    if day == '00':
                        expiration_dates = datetime(2000 + int(year), int(month), 1)
                    else:
                        expiration_dates = datetime(2000 + int(year), int(month), int(day))
                else:
                    expiration_dates = False

                stander = rec.barcode[0:2]
                if stander == '01':
                    rec.global_barcode = rec.barcode[2:16]
                else:
                    rec.global_barcode = False
                # start_global_barcode = rec.barcode[0:1]
                rec.barcode_date = barcode_date_num
                rec.expiration_dates = expiration_dates
                batch_value = barcode[26:]
                srial_list = batch_value.split( '240')
                srial_list1 = batch_value.split( '30')
                srial_list2 = batch_value.split( '21')
                if len(srial_list) > 1:
                    rec.lot_name = srial_list[0]
                    rec.serial_no = srial_list[1]
                if len(srial_list1) > 1:

                    rec.lot_name = srial_list1[0]
                    rec.serial_no = srial_list1[1]
                if len(srial_list2) > 1:
                    rec.lot_name = srial_list2[0]
                    rec.serial_no = srial_list2[1]
                else:
                    rec.qty_done = 1

            else:
                rec.barcode = rec.barcode
                rec.global_barcode = ""
                rec.lot_name = ""
                rec.barcode_date = ""
                rec.serial_no = ""
                rec.expiration_dates = False

    @api.constrains('global_barcode')
    def _check_global_barcode(self):
        for line in self:
            if line.global_barcode != line.product_id.barcode and line.global_barcode:
                raise ValidationError(_('Not The Same Gobal Bar Code For This Product !'))


