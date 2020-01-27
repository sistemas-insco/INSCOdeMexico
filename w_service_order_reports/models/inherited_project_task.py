# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2019 Wedoo - https://wedoo.tech
# All Rights Reserved.
#
# Developer(s): Sergio Ernesto Tostado Sánchez
#               (sts@wedoo.tech)
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

from odoo import api, fields, models, _


class ProjectTask(models.Model):

    _inherit = "project.task"

    service_order = fields.Char(
        string="Service Order",
        help="Service Order for this task."
    )

    @api.model
    def getServiceOrders(self, docs, no_sequence=True):
        if no_sequence:
            docs_needs_serv_order = docs.filtered(lambda r: not r.service_order)
            if docs_needs_serv_order:
                next_serv_order = self.env['ir.sequence'].next_by_code(
                    'service.order')
                docs_needs_serv_order.write({
                    'service_order': next_serv_order
                })
        service_orders = ", ".join(
            set([task.service_order for task in docs if task.service_order]))
        procedures = ", ".join(set(
            [task.sale_line_id.product_id.product_tmpl_id.process for task in docs if task.sale_line_id.product_id.product_tmpl_id.process]))
        # init for second list in first iteration after the list principal
        # and join exclude duplicates
        tags = ",".join(set(
            [tag.name for task in docs for tag in task.tag_ids]))
        service_types = [
            {
                'service': task.sale_line_id.name,
                'product_id': task.sale_line_id.product_id,
                'origin': task.service_order,
                'qty': task.sale_line_id.product_uom_qty,
                'description': task.get_description_text(),
                'procedures': procedures,
                'tags': tags
                } for task in docs]
        return docs[0].with_context({
            'service_orders': service_orders,
            'service_types': service_types
        })

    @api.model
    def get_services_description(self, docs):
        service_orders = ", ".join(set(
            [task.service_order for task in docs if task.service_order]))
        procedures = ", ".join(set(
            [task.sale_line_id.product_id.product_tmpl_id.process for task in docs if task.sale_line_id.product_id.product_tmpl_id.process]))
        service_types = [
            {   'service_orders': service_orders,
                'service': task.sale_line_id.name,
                'qty': task.sale_line_id.product_uom_qty,
                'procedures': procedures,
                'origin': task.service_order} for task in docs]
        return {'service_types': service_types}
