from openerp import api, fields, models
import time

class galery(models.Model):
	_name = 'vit.galery'

	name = fields.Char(string="Name", required=True)

	description = fields.Text(string="Description")

	date_time  = fields.Date(string="Date", required=True, )

	image_ids = fields.One2many(comodel_name="vit.galery_image", inverse_name="galery_id", string="Image", ondelete="cascade")

	image = fields.Binary(string="Image", compute="get_image")

	def get_image(self):
		for rec in self:
			ambil_gambar   = self.env['vit.galery_image'].search([('id','=',rec.image_ids[0].id)])
			rec.image      = ambil_gambar.image