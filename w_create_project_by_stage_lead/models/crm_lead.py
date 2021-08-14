# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2018 Wedoo - http://www.wedoo.tech/
# All Rights Reserved.
#
# Developer(s): Ernesto García Medina
#               (ernesto.garcia@telematel.com)
#
########################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################

from odoo import api, fields, models, tools, _


class CrmLead(models.Model):

    _inherit = 'crm.lead'
    
    #@api.multi
    def write(self, vals):
        stage_obj = self.env['crm.stage']
        project_obj = self.env['project.project']
        task_obj = self.env['project.task']
        for lead in self:
            if 'stage_id' in vals:
                stage_id = stage_obj.browse(vals.get('stage_id'))
                if stage_id.create_project:
                    project_values = {
                        'name': lead.name,
                        'privacy_visibility': stage_id.privacy_visibility
                    }
                    project = project_obj.sudo().create(project_values)
                    vals['project_id'] = project.id
                    for stage in stage_id.project_stage_ids:
                        stage.sudo().write({'project_ids': [(4, project.id)]})
                    for task in stage_id.default_task_ids:
                        task_vals = {
                            'name': task.name,
                            'project_id': project.id,
                            'department_id': task.department_id.id
                        }
                        task_obj.sudo().create(task_vals)
        return super(CrmLead, self).write(vals)

    project_id = fields.Many2one(
        'project.project',
        string = 'Project',
        help = _('Project related to this opportunity.'),
        track_visibility="onchange"
    )

class CrmStage(models.Model):

    _inherit = 'crm.stage'

    create_project = fields.Boolean("Create project?")
    privacy_visibility = fields.Selection([
            ('followers', _('On invitation only')),
            ('employees', _('Visible by all employees')),
            ('portal', _('Visible by following customers')),
        ],
        string='Privacy', required=True,
        default='employees',
        help="Holds visibility of the tasks or issues that belong to the current project:\n"
                "- On invitation only: Employees may only see the followed project, tasks or issues\n"
                "- Visible by all employees: Employees may see all project, tasks or issues\n"
                "- Visible by following customers: employees see everything;\n"
                "   if website is activated, portal users may see project, tasks or issues followed by\n"
                "   them or by someone of their company\n")
    project_stage_ids = fields.Many2many('project.task.type', 'project_task_default_type_rel', 'type_id', 'stage_id',)
    default_task_ids = fields.One2many('crm.stage.default.task', 'stage_id')
