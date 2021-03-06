# -*- coding: utf-8 -*-
import logging

import booby
from booby import Model
from booby.fields import Integer, Float, String, Embedded

logger = logging.getLogger('validators')


class Party(Model):
    nif = String(required=True)
    name = String(required=True)
    uri = String()


class Contractor(Party):
    pass


class Contracted(Party):
    pass


class Licitation(Model):
    uuid = String(required=True)
    file = String()
    title = String()

    type = String()
    subtype = String()
    result_code = String()

    amount = Float()
    payable_amount = Float()

    budget_amount = Float()
    budget_payable_amount = Float()

    issued_at = String(required=True)
    awarded_at = String(required=True)
    contractor = Embedded(Contractor, required=True)
    contracted = Embedded(Contracted, default=None)


def validate(data):
    model = Licitation(**data)
    if model.is_valid:
        return dict(model)
    else:
        logger.error(dict(model.validation_errors))
