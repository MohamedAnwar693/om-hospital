# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.sale.models.sale_order import SaleOrder as OdooSaleOrder


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description', required=True)

    # def unlink(self):
    #     print("done..........")
    #     return super(OdooSaleOrder, self).unlink()


def unlink(self):
    return super(OdooSaleOrder, self).unlink()


OdooSaleOrder.unlink = unlink
