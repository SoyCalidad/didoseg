from odoo import http
from odoo.http import request
from odoo.addons.website_hr_recruitment.controllers.main import WebsiteHrRecruitment
from werkzeug.exceptions import NotFound


class WebsiteHrRecruitmentExtended(WebsiteHrRecruitment):

    def job(self, job, **kwargs):
        if job.is_job_position_closed:
            raise NotFound()
        return super().job(job, **kwargs)

    def jobs_apply(self, job, **kwargs):
        if job.is_job_position_closed:
            raise NotFound()
        return super().jobs_apply(job, **kwargs)
