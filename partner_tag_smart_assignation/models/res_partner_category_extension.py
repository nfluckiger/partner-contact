from odoo import fields, models, api


class ResPartnerCategoryExtension(models.Model):
    _inherit = "res.partner.category"

    author_of_the_tag = fields.Many2one('res.users', string="Author")
    department_that_uses_the_tag = fields.Many2one('hr.department', string="Department")
    description_of_the_tag = fields.Text(string="Description")
    valid_until = fields.Date(string="Valid until")

    @api.model
    def _check_validity_dates(self):
        """ Scheduled method to deactivate records past their validity date """
        today = fields.Date.today()
        records_to_deactivate = self.search([('valid_until', '<', today), ('active', '=', True)])
        records_to_deactivate.write({'active': False})

        records_to_activate = self.search([('valid_until', '>', today), ('active', '=', False)])
        records_to_activate.write({'active': True})


