from odoo import http
from odoo.http import request
from odoo.addons.website_hr_recruitment.controllers.main import WebsiteHrRecruitment
from werkzeug.exceptions import NotFound


class WebsiteHrRecruitmentExtended(WebsiteHrRecruitment):

    @http.route()
    def job(self, job, **kwargs):
        if job.is_job_position_closed:
            raise NotFound()
        return super().job(job, **kwargs)

    @http.route()
    def jobs_apply(self, job, **kwargs):
        if job.is_job_position_closed:
            raise NotFound()
        return super().jobs_apply(job, **kwargs)
