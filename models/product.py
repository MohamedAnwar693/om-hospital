from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[
        ('test', 'Test'), ('service',)
        ], tracking=True, ondelete={'test': 'cascade'})
