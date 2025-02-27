from odoo import models
import base64
import io


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_id_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Patient ID Card')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#3091FA'})
        row = 0
        col = 0
        sheet.set_column('A:A', 12)
        sheet.set_column('B:B', 10)

        for obj in partners:
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'ID Card', format_1)

            row += 1
            if obj.image:
                patient_image = io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "image.png", {'image_data': patient_image, 'x_scale': 0.5, 'y_scale': 0.5})

            row += 8
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col + 1, obj.name)
            row += 1
            sheet.write(row, col, 'Age', bold)
            sheet.write(row, col + 1, obj.age)
            row += 1
            sheet.write(row, col, 'Reference', bold)
            sheet.write(row, col + 1, obj.reference)






























