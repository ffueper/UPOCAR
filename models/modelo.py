'''
Created on 27 nov. 2019

@author: usuario
'''

from odoo import models, fields, api

class modelo(models.Model):
    _name = 'upocar.modelo'
    
    nombre_modelo = fields.Char('Nombre', size=64, required=True)
    
    marca_ids = fields.Many2many("upocar.marca", string="Marca del modelo")