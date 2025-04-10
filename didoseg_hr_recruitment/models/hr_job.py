from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Job(models.Model):
    _inherit = 'hr.job'

    is_job_position_closed = fields.Boolean(
        string='Is Job Position Closed', default=False,
        help='The position will remain visible on the website, but visitors will not be able to apply.',
    )
