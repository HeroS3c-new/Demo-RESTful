# coding: utf-8

"""
    DEMO API Restful

    API realizzata per presentare una demo di funzionamento RESTful Sistemi paralelli e distributiti (flipped lessons) anno: 2022/2023   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2001(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'nome': 'str',
        'dipartimento': 'str'
    }

    attribute_map = {
        'id': 'id',
        'nome': 'nome',
        'dipartimento': 'dipartimento'
    }

    def __init__(self, id=None, nome=None, dipartimento=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._nome = None
        self._dipartimento = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if nome is not None:
            self.nome = nome
        if dipartimento is not None:
            self.dipartimento = dipartimento

    @property
    def id(self):
        """Gets the id of this InlineResponse2001.  # noqa: E501

        ID del corso  # noqa: E501

        :return: The id of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2001.

        ID del corso  # noqa: E501

        :param id: The id of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nome(self):
        """Gets the nome of this InlineResponse2001.  # noqa: E501

        Nome del corso  # noqa: E501

        :return: The nome of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """Sets the nome of this InlineResponse2001.

        Nome del corso  # noqa: E501

        :param nome: The nome of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._nome = nome

    @property
    def dipartimento(self):
        """Gets the dipartimento of this InlineResponse2001.  # noqa: E501

        Dipartimento del corso.  # noqa: E501

        :return: The dipartimento of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._dipartimento

    @dipartimento.setter
    def dipartimento(self, dipartimento):
        """Sets the dipartimento of this InlineResponse2001.

        Dipartimento del corso.  # noqa: E501

        :param dipartimento: The dipartimento of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._dipartimento = dipartimento

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2001, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other