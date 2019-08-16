# -*- coding: utf-8 -*-
import logging

import werkzeug.utils

from odoo import http
from odoo.http import request
from odoo.addons.documents.controllers.main import ShareRoute  # Import the class
from odoo.tools import consteq

logger = logging.getLogger(__name__)

class CustomShareRoute(ShareRoute):
    # share portals route.
    @http.route(['/document/share/<int:share_id>/<token>'], type='http', auth='public')
    def share_portal(self, share_id=None, token=None, **kwargs):
        env = request.env
        try:
            logger.debug("call CustomShareRoute")
            logger.debug("share_id : %s, token : %s", share_id, token)
            share = env['documents.share'].sudo().browse(share_id)
            logger.debug("security_type : %s", share.security_type)
            if share.security_type == 'users':
                if not request.session.uid:
                    return werkzeug.utils.redirect('/web/login?redirect=/document/share/%s/%s' % (share_id, token))
                else:
                    if not share.security_user_ids or request.session.uid not in share.security_user_ids.ids:
                        return request.render('linkup_documents.access_denied')
            elif share.security_type == 'password':
                password = kwargs.get('password')
                logger.debug("password : [%s]", password)
                logger.debug("share.security_password : [%s]", share.security_password)
                if not password or not consteq(password,share.security_password):
                    options = {
                        'token': str(token),
                        'share_id': str(share.id),
                    }
                    return request.render('linkup_documents.share_password', options)
            res = super(CustomShareRoute, self).share_portal(share_id, token)
            return res
        except Exception:
            logger.exception("Failed to generate the multi file share portal")
        return request.not_found()

