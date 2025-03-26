from odoo import fields, models, api
from odoo.exceptions import ValidationError



class Profession(models.Model):
    _name = 'res.partner.profession'
    _description = 'Profession'

    name = fields.Char(string='Name')


class Faculty(models.Model):
    _name = 'res.partner.faculty'
    _description = 'Faculty'

    name = fields.Char(string='Name')


class Occupation(models.Model):
    _name = 'res.partner.occupation'
    _description = 'Occupation'

    partner_id = fields.Many2one('res.partner', string='Partner')
    profession_id = fields.Many2one('res.partner.profession', string='Profession')
    faculty_id = fields.Many2one('res.partner.faculty', string='Faculty')


class EmploymentStatus(models.Model):
    _name = 'res.partner.employment_status'
    _description = 'Employment Status'

    name = fields.Char(string="Status", required=True)


class WorkExperience(models.Model):
    _name = 'res.partner.work_experience'
    _description = 'Work Experience'

    partner_id = fields.Many2one('res.partner', string='Partner')
    job_position = fields.Char(string='Job Position')
    company = fields.Char(string='Company')
    state_id = fields.Many2one('res.country.state', string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id and self.country_id != self.state_id.country_id:
            self.state_id = False

    @api.onchange('state_id')
    def _onchange_state(self):
        if self.state_id.country_id and self.country_id != self.state_id.country_id:
            self.country_id = self.state_id.country_id


class ResPartner(models.Model):
    _inherit = 'res.partner'

    occupation_ids = fields.One2many('res.partner.occupation', 'partner_id', string='Occupation')
    employment_status_id = fields.Many2one('res.partner.employment_status', string='Employment Status')
    description = fields.Text(string='Description')

    personal_email = fields.Char(string='Personal Email')
    professional_email = fields.Char(string='Professional Email')
    social_twitter = fields.Char('X Account')
    social_facebook = fields.Char('Facebook Account')
    social_github = fields.Char('GitHub Account')
    social_linkedin = fields.Char('LinkedIn Account')
    social_youtube = fields.Char('Youtube Account')
    social_instagram = fields.Char('Instagram Account')
    social_tiktok = fields.Char('TikTok Account')

    work_experience_ids = fields.One2many('res.partner.work_experience', 'partner_id', string='Work Experience')
