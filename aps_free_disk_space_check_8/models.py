# -*- coding: utf-8 -*-
# billm@ap-accounting.co.za

from openerp import models, fields, api
import datetime 
import os

import logging
_logger = logging.getLogger(__name__)

class res_company(models.Model):   
    _inherit = "res.company"

    @api.model
    def free_disk_space_check_cron(self):
        st = os.statvfs("/")
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        free_percentage = int(free * 100 / total)
        _logger.info('Free Disk space is ' + str(free_percentage) + '%')
        todayDate = datetime.date.today()
        if free_percentage < 20 or todayDate.day == 17:
            companies = self.env['res.company'].search([])
            for company in companies:
                mail_smtp_server = self.env['ir.mail_server'].search( [])
                if mail_smtp_server and company.email:
                    email_vals = {'state': 'outgoing',
                                'subject': 'Disk ' + str(free_percentage) + '% free',
                                'body_html':'Odoo 8 server free disk space : <br />'+ str(company.name) + '<br />' + str(company.street) + '<br />' + str(company.street2) + '<br />' + str(company.city) + '</p>',
                                'email_to': company.email,
                                'email_from': 'support@ap-accounting.co.za'}
                    self.env['mail.mail'].create(email_vals)

res_company()               

    