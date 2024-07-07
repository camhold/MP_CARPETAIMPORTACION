from odoo import models, fields, api


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    is_account_import = fields.Boolean(string="Es cuenta de importacion?")

    def close_account_import_button(self):
        for analytic_id in self:
            amount_total = 0
            product_tmpl_id = self.env['product.template']
            for line_id in analytic_id.line_ids:
                amount_total += line_id.amount
                if line_id.product_id.product_tmpl_id.detailed_type == 'product':
                    product_tmpl_id = line_id.product_id.product_tmpl_id
            if product_tmpl_id:
                product_tmpl_id.standard_price = abs(amount_total)
