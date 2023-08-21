from odoo import fields, models


class ResPartnerCategoryExtension(models.Model):
    _inherit = "res.partner.category"

    author_of_the_tag = fields.Char(string="Author")
    department_that_uses_the_tag = fields.Char(string="Department")
    description_of_the_tag = fields.Text(string="Description")
    is_unlimited_tag = fields.Boolean(string="Unlimited")
