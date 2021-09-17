from http import HTTPStatus

import pytest
import logging

from string import Template

from hamcrest import *
from .api import ApiAlaska
from .bear import BearAlaska

LOGGER = logging.getLogger(__name__)
api = ApiAlaska()


@pytest.fixture(scope="session")
def base_url():
    yield 'http://localhost:8091'


def has_content(item):
    return has_property('text', contains_string(item))


def has_status(status):
    return has_property('status_code', equal_to(status))


@pytest.fixture(params=[{'bear_type': None, 'bear_name': None}])
def bear_json(request, base_url):
    bear_type = request.param.get('bear_type')
    bear_name = request.param.get('bear_name')
    bear_info = BearAlaska(bear_type=bear_type, bear_name=bear_name).__dict__
    return bear_info


@pytest.fixture(params=[{'bear_type': None, 'bear_name': None}])
def bear(request, base_url):
    """
    Fixture for creating bear and deleting it in teardown

    Args:
        request: object
        base_url: base url
    """
    bear_list = []

    def create_bear():
        bear_type = request.param.get('bear_type')
        bear_name = request.param.get('bear_name')
        bear_info = BearAlaska(bear_type=bear_type, bear_name=bear_name).__dict__
        LOGGER.info(bear_info)

        response = api.create_bear(base_url=base_url, bear_json=bear_info)
        assert_that(response, has_status(HTTPStatus.OK))
        LOGGER.info(response)

        bear_info["bear_id"] = response.content.decode()
        bear_list.append(bear_info)
        return bear_info

    def delete_bear():
        for bear in bear_list:
            api.delete_bear_by_id(base_url=base_url, bear_id=bear["bear_id"])

    request.addfinalizer(delete_bear)
    return create_bear


def is_bears_info_identical(actual_bear_info, expected_bear_info):
    """
    Fixture for comparing bears info

    Args:
        actual_bear_info: actual bear info in json
        expected_bear_info: expected bear info in json
    """

    msg_template = Template('Expected $field_name: $expected_value, but actual $field_name is $actual_value')

    bear_id = actual_bear_info.get('bear_id') == int(expected_bear_info.get('bear_id'))
    bear_type = actual_bear_info.get('bear_type') == expected_bear_info.get('bear_type')
    bear_name = actual_bear_info.get('bear_name') == expected_bear_info.get('bear_name')
    bear_age = actual_bear_info.get('bear_age') == expected_bear_info.get('bear_age')

    if not bear_id:
        LOGGER.error(msg_template.substitute(field_name='bear_id', actual_value=actual_bear_info.get('bear_id'),
                                             expected_value=expected_bear_info.get('bear_id')))
    if not bear_type:
        LOGGER.error(msg_template.substitute(field_name='bear_type', actual_value=actual_bear_info.get('bear_type'),
                                             expected_value=expected_bear_info.get('bear_type')))
    if not bear_name:
        LOGGER.error(msg_template.substitute(field_name='bear_name', actual_value=actual_bear_info.get('bear_name'),
                                             expected_value=expected_bear_info.get('bear_name')))
    if not bear_age:
        LOGGER.error(msg_template.substitute(field_name='bear_age', actual_value=actual_bear_info.get('bear_age'),
                                             expected_value=expected_bear_info.get('bear_age')))
    return bear_id and bear_type and bear_name and bear_age
