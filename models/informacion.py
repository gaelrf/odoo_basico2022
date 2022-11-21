# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class información(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para infomacion'

    name = fields.Char(string="Título:")
    descripcion = fields.Text(string="A descripción:")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    peso = fields.Float(string="Peso en kgs", digits=(6, 2), default=4.3)
    sexo_traducido = fields.Selection([("Hombre", "Home"), ("Mujer", "Muller"), ("Otro", "Outro")], string="sexo")
    alto_en_cms = fields.Integer(string="Alto en Centímetros:")
    ancho_en_cms = fields.Integer(string="Ancho en Centímetros:")
    longo_en_cms = fields.Integer(string="Longo en Centímetros:")
    volume = fields.Float(compute="_volume", string="Volume en Metros Cúbicos", digits=(6, 6), store=True)
    densidade = fields.Float(compute="_densidade", string="Densidade en Kgs/Metros Cúbicos", store=True)
    literal = fields.Char(store=False)

    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = (float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) *
                               float(rexistro.ancho_en_cms)) / 1000000


    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = rexistro.peso / rexistro.volume
            else:
                rexistro.densidade = 0


    @api.onchange('alto_en_cms')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
            else:
                rexistro.literal = ""


    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 6:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 6 ' % rexistro.name)
