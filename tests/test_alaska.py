from tests.conftest import *
from hamcrest import assert_that, all_of

import json


class TestAlaska:
    bear_types = BearAlaska.BEAR_TYPES
    params = [{"bear_type": bear_type} for bear_type in bear_types]

    @pytest.mark.parametrize('bear', params, indirect=['bear'], ids=bear_types)
    def test_create_bear_with_type_and_get_info(self, base_url, bear):
        """
        Check creating bear with type

        Args:
            base_url: base url
            bear: fixture for creating bear
        """

        bear = bear()

        response = api.get_bear_by_id(base_url=base_url, bear_id=bear['bear_id'])
        actual_bear_info = json.loads(response.content.decode())
        assert_that(response, has_status(HTTPStatus.OK))
        assert actual_bear_info is not None
        assert is_bears_info_identical(actual_bear_info=actual_bear_info, expected_bear_info=bear)

    @pytest.mark.parametrize('bear_json', [{"bear_type": BearAlaska.WRONG_TYPE}], indirect=['bear_json'])
    def test_create_bear_with_wrong_type(self, base_url, bear_json):
        """
        Check creating bear with type

        Args:
            base_url: base url
            bear_json: fixture for creating bear
        """

        response = api.create_bear(base_url=base_url, bear_json=bear_json)
        assert_that(response, has_status(HTTPStatus.INTERNAL_SERVER_ERROR))

    def test_delete_bear(self, base_url, bear):
        """
        Check deleting bear

        Args:
            base_url: base url
            bear: fixture for creating bears
        """
        bear = bear()
        response = api.delete_bear_by_id(base_url=base_url, bear_id=bear["bear_id"])
        assert_that(response, has_status(HTTPStatus.OK))

        response = api.get_bear_by_id(base_url=base_url, bear_id=bear["bear_id"])
        assert_that(response, all_of(
            has_status(HTTPStatus.OK),
            has_content(api.EMPTY)
        ))

    bear_update_tests_ids = ['new_bear_type: ' + BearAlaska.BLACK_TYPE,
                             'new_bear_type: ' + BearAlaska.GUMMY_TYPE,
                             'new_bear_name: ' + 'new name',
                             'new_bear_name: ' + 'New Name',
                             'new_bear_name: ' + 'NEW NAME']

    @pytest.mark.parametrize('new_bear_attrs', [{'bear_type': BearAlaska.BLACK_TYPE},
                                                {'bear_type': BearAlaska.GUMMY_TYPE},
                                                {'bear_name': 'new name'},
                                                {'bear_name': 'New Name'},
                                                {'bear_name': 'NEW NAME'}], ids=bear_update_tests_ids)
    def test_updating_bear(self, base_url, bear, new_bear_attrs):
        """
        Check updating bear info

        Args:
            base_url: base url
            bear: fixture for creating bears
            new_bear_attrs: new bear attributes
        """

        bear = bear()
        LOGGER.critical(f"Created bear: {bear}")

        bear.update(new_bear_attrs)
        LOGGER.critical(f"Updated bear info: {bear}")

        response = api.update_bear_by_id(base_url=base_url, bear_id=bear["bear_id"], bear_json=bear)
        assert_that(response, has_status(HTTPStatus.OK))

        response = api.get_bear_by_id(base_url=base_url, bear_id=bear["bear_id"])
        assert_that(response, has_status(HTTPStatus.OK))
        actual_bear_info = json.loads(response.content)
        LOGGER.critical(f"Updated bear: {actual_bear_info}")

        assert is_bears_info_identical(actual_bear_info=actual_bear_info, expected_bear_info=bear)

    def test_getting_all_bears_info(self, base_url, bear):
        """
        Check getting all bears info

        Args:
            base_url: base url
            bear: fixture for creating bears
        """

        bear1 = bear()
        bear2 = bear()

        response = api.get_all_bears(base_url=base_url)
        assert_that(response, has_status(HTTPStatus.OK))

        bears_info = json.loads(response.content)
        LOGGER.critical(f"All bears info: {bears_info}")

        for bear in bears_info:
            if bear['bear_id'] == int(bear1['bear_id']):
                assert is_bears_info_identical(actual_bear_info=bear, expected_bear_info=bear1)
            elif bear['bear_id'] == int(bear2['bear_id']):
                assert is_bears_info_identical(actual_bear_info=bear, expected_bear_info=bear2)
            else:
                pytest.fail(f"Actual bears info is different from expected")

    def test_deleting_all_bears(self, base_url, bear):
        """
        Check deleting all bears

        Args:
            base_url: base url
            bear: function for creating bear
        """

        bear1 = bear()
        bear2 = bear()

        response = api.delete_all_bears(base_url=base_url)
        assert_that(response, all_of(
            has_status(HTTPStatus.OK),
            has_content(api.OK)))

        bear1_info = api.get_bear_by_id(base_url=base_url, bear_id=bear1["bear_id"])
        bear2_info = api.get_bear_by_id(base_url=base_url, bear_id=bear2["bear_id"])
        all_bears_info = api.get_all_bears(base_url=base_url)

        assert_that(bear1_info, has_content(api.EMPTY))
        assert_that(bear2_info, has_content(api.EMPTY))
        assert_that(all_bears_info, has_content('[]'))
