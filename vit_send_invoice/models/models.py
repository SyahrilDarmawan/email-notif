# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_send_invoice(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    def action_post(self):
        super(vit_send_invoice, self).action_post()
        # Send email after post
        self.action_send_email()
        return True

    def action_send_email(self):
        template = self.env.ref('vit_send_invoice.email_notif_post')

        try:
            values = template.generate_email(self.id, ['subject', 'email_from', 'partner_to', 'body_html'])
            print("Rendered Values:", values)

            # Siapkan email values (opsional override)
            email_values = {
                'subject': self.name,
                'email_from': values.get('email_from') or 'admin@yourcompany.com',
                'email_to': self.partner_id.email,
                'body_html': values.get('body_html') or '<div>Email body failed to render.</div>',
            }

            template.send_mail(self.id, force_send=True, email_values=email_values)

        except Exception as e:
            print("Error sending email:", str(e))

        return True



        # template = self.env.ref('vit_send_invoice.email_notif_post')
        # if template:
        #     # Debug data
        #     print("Invoice ID:", self.id)
        #     print("Invoice Name:", self.name)
        #     print("Partner ID:", self.partner_id.id if self.partner_id else "No Partner")
        #     print("Partner Name:", self.partner_id.name if self.partner_id else "No Partner Name")
        #     print("User Email:", self.user_id.email if self.user_id else "No User Email")
        #     print("Partner Email:", self.partner_id.email if self.partner_id else "No Partner Email")
        #
        #     # Generate email values from template
        #     try:
        #         values = template.generate_email(self.id, ['subject', 'email_from', 'partner_to', 'body_html'])
        #         print("Rendered Values:", values)
        #
        #         # Prepare mail values
        #         mail_values = {
        #             'subject': values.get('subject') or 'Invoice Notification',
        #             'email_from': values.get('email_from') or 'admin@yourcompany.com',
        #             'email_to': self.partner_id.email if self.partner_id else False,
        #             'body_html': values.get('body_html') or '<div>Email body failed to render.</div>',
        #             'auto_delete': False,
        #         }
        #
        #         # Create and send email
        #         mail = self.env['mail.mail'].create(mail_values)
        #         mail.send()
        #     except Exception as e:
        #         print("Error sending email:", str(e))
        # else:
        #     print("Template not found!")






        
    #    # Buat body HTML secara manual
    #     body_html = f"""
    #         <div>
    #             Halo <strong>{self.partner_id.name or 'Dear Partner'}</strong>,
    #             <br/>
    #             Invoice Anda <strong>#{self.name}</strong> telah divalidasi!
    #             <br/>
    #             Terima Kasih,
    #             <br/>
    #             Tim Admin
    #         </div>
    #     """
        
    #     # Ambil template dasar
    #     template = self.env.ref('vit_send_invoice.email_notif_post')
        
    #     # Kirim email dengan body yang sudah dibuat
    #     email_values = {
    #         'body_html': body_html,
    #         'subject': self.name, 
    #         'email_to': self.partner_id.email, 
    #     }
    #     template.send_mail(self.id, force_send=True, email_values=email_values)


        

    
        #############################################################################################

        # template = self.env.ref('vit_send_invoice.email_notif_post')
        # template.send_mail(self.id, force_send=True)

        #############################################################################################

        
        



        