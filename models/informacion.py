# -*- coding: utf-8 -*-


from odoo import models, fields, api

class información(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'Exemplo para infomacion'

     name = fields.Char(string="Título:")
     descripcion = fields.Text(string="A descripción:")
     autorizado = fields.Boolean(string="¿Autorizado?")
     peso = fields.Float(string="Peso en kgs",digits=(6,2),default=4.3)
     sexo_traducido = fields.Selection([("Hombre","Home"),("Mujer","Muller"),("Otro","Outro")],string="sexo")
     alto_en_cms = fields.Integer(string="Alto en Centímetros:")
     ancho_en_cms = fields.Integer(string="Ancho en Centímetros:")
     longo_en_cms = fields.Integer(string="Longo en Centímetros:")
     volume = fields.Float(compute="_volume", store=True)
     densidade = fields.Float(compute="_densidade", store=True)

     @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
     def _volume(self):
          for rexistro in self:
               rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(
                    rexistro.ancho_en_cms)
     @api.depends('peso', 'volume')
     def _densidade(self):
          for rexistro in self:
               if rexistro.volume!=0:
                    rexistro.densidade = rexistro.peso / rexistro.volume
               else:
                    rexistro.densidade = 0
