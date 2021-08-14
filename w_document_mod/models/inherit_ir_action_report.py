from odoo import models, fields, api, _
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import io
from os.path import join
import base64
from odoo.exceptions import UserError


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    #@api.multi
    def _post_pdf(self, save_in_attachment, pdf_content=None, res_ids=None):
        # OVERRIDE
        if self.model == 'sale.order' and res_ids and len(
            res_ids) == 1 and self.id == self.env.ref(
                'sale.action_report_saleorder').id:
            # Add attachment.
            get_param =  self.env['ir.config_parameter'].sudo().get_param
            # get pdf on b64
            default_terms_file = get_param('w_document_mod.terms_file')
            default_filename_terms = get_param(
                'w_document_mod.filename_terms')
            if not default_filename_terms or not default_terms_file:
                return super(IrActionsReport, self)._post_pdf(
                    save_in_attachment=save_in_attachment,
                    pdf_content=pdf_content, res_ids=res_ids)
            else:
                extend = False
                if '.' in default_filename_terms:
                    extend = default_filename_terms.split(".")[1]
                else:
                    raise UserError(_(
                        'The extension of the file of terms and conditions '
                        'that is configured by default is not (.pdf)'))
                if not extend or extend != 'pdf':
                    raise UserError(_(
                        'Make sure that the file is attached to the pdf file and has '
                        'its own extension (.pdf), otherwise it will not be able to '
                        'save the changes.'))
                # decode b64
                bin_value = base64.b64decode(default_terms_file)
                # create pdf bin
                pdf_content_terms = io.BytesIO(bin_value)
                reader_buffer = io.BytesIO(pdf_content)
                writer = PdfFileWriter()
                streams = []
                streams.append(reader_buffer)
                streams.append(pdf_content_terms)
                if len(streams) == 1:
                    pdf_content = reader_buffer.getvalue()
                    return super(IrActionsReport, self)._post_pdf(
                        save_in_attachment=save_in_attachment,
                        pdf_content=pdf_content, res_ids=res_ids)
                else:
                    for stream in streams:
                        reader = PdfFileReader(stream)
                        writer.appendPagesFromReader(reader)
                    result_stream = io.BytesIO()
                    streams.append(result_stream)
                    writer.write(result_stream)
                    result = result_stream.getvalue()
                    pdf_content = result
                    return super(IrActionsReport, self)._post_pdf(
                        save_in_attachment=save_in_attachment,
                        pdf_content=pdf_content, res_ids=res_ids)
        else:
            return super(IrActionsReport, self)._post_pdf(
                    save_in_attachment=save_in_attachment,
                    pdf_content=pdf_content, res_ids=res_ids)