# -*- coding:utf-8 -*-

from lxml import etree


class XmlResponseDescriptor(object):

    def __init__(self, xpath):
        self._xpath = xpath
        self._xml_response = None

    def __get__(self, instance, owner):

        result = None
        try:
            self._xml_response = etree.fromstring(instance._text_response)
            result = self._xml_response.xpath(self._xpath)
        except Exception as err:
            print(err)
        finally:
            if isinstance(result, list):
                return etree.tostring(result[0])
            else:
                return result


class Answer(object):

    def __init__(self, text_response):
        self._text_response = text_response

    heading = XmlResponseDescriptor('.//Heading/text()')
    image = XmlResponseDescriptor('.//Image/text()')
    abstract = XmlResponseDescriptor('.//Abstract/text()')
    related_topics = XmlResponseDescriptor('.//RelatedTopics')


