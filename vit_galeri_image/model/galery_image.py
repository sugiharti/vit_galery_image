from openerp import api, fields, models
import time

class galery_image(models.Model):
	_name = 'vit.galery_image'

	galery_id = fields.Many2one(comodel_name="vit.galery",
										string="Galery Name")
	name_image  = fields.Char(string="Name", required=True)
	image = fields.Binary(string="Image")

# class galery_image(osv.osv):
# 	_name = 'vit.galery_image'
# 	_columns = {
# 		'galery_id'	   : fields.many2one('vit.galery', string='Galery Id'),
# 		'name'         : fields.many2one('vit.galery', string='Galery Name'),
# 		'name_image'   : fields.char('Name', size=100, required=True),
# 		'image'        : fields.binary('Image')
# 	}