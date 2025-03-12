# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vit_send_invoice(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    def action_post(self):
        super(vit_send_invoice, self).action_post()

        # send email after post
        self.action_send_email()

        return False

    def action_send_email(self):
        # Buat body HTML secara manual
        body_html = f"""
            <div>
                Halo <strong>{self.partner_id.name or 'Dear Partner'}</strong>,
                <br/>
                Invoice Anda <strong>#{self.name}</strong> telah divalidasi!
                <br/>
                Terima Kasih,
                <br/>
                Tim Admin
            </div>
        """
        
        # Ambil template dasar
        template = self.env.ref('vit_send_invoice.email_notif_post')
        
        # Kirim email dengan body yang sudah dibuat
        email_values = {
            'body_html': body_html,
            'subject': self.name,  # Pastikan subject juga sesuai
            'email_to': self.partner_id.email,  # Pastikan email penerima
        }
        template.send_mail(self.id, force_send=True, email_values=email_values)