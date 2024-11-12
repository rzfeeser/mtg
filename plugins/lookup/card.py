# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
  name: card
  author: RZFeeser (@rzfeeser) <z@rzfeeser.com>
  version_added: "1.1"  # for collections, use the collection version, not the Ansible version
  short_description: make mtg card lookup by name
  description:
      - This lookup returns the json associated with a mtg card
  options:
    _terms:
      description: path(s) of files to read
      required: True
    option1:
      description:
            - Sample option that could modify plugin behavior.
            - This one can be set directly ``option1='x'`` or in ansible.cfg, but can also use vars or environment.
      type: string
      ini:
        - section: file_lookup
          key: option1
  notes:
    - if read in variable context, the file can be interpreted as YAML if the content is valid to the parser.
    - this lookup does not understand globbing --- use the fileglob lookup instead.
"""
import requests

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

      # First of all populate options,
      # this will already take into account env vars and ini config
      self.set_options(var_options=variables, direct=kwargs)

      # lookups in general are expected to both take a list as input and output a list
      # this is done so they work with the looping construct 'with_'.
      ret = []
      for term in terms:
          display.debug(f"File lookup term: {term}")

          # Find the file in the expected search path, using a class method
          # that implements the 'expected' search path for Ansible plugins.
          ### lookupfile = self.find_file_in_search_path(variables, 'files', term)

          # Don't use print or your own logging, the display class
          # takes care of it in a unified way.
          display.vvvv(term)
          url_to_lookup = "https://api.magicthegathering.io/v1/cards?name=" + term
          
          display.vvvv(f"Making lookup to {url_to_lookup}") # displays on -vvvv
          try:
              if term:
                  resp = requests.get(url_to_lookup)
                  if resp.status_code != 200:
                      raise AnsibleParseError()
                  ret.append(resp.json())
              else:
                  # Always use ansible error classes to throw 'final' exceptions,
                  # so the Ansible engine will know how to deal with them.
                  # The Parser error indicates invalid options passed
                  raise AnsibleParserError()
          except AnsibleParserError:
              raise AnsibleError(f"problem looking up {term}")

          # consume an option: if this did something useful, you can retrieve the option value here
          if self.get_option('option1') == 'do something':
            pass

      return ret
