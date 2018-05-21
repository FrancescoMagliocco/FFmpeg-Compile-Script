#!/usr/bin/env python3
"""Repository Base"""

import logging
import os
import sys
from enum import Enum
from abc import ABC, abstractmethod
from pathlib import Path
from typing import NamedTuple

class Options:

    # Using a 'NamedTuple' instead of a regular class because I want these
    #   members to be constant.
    class _Option(NamedTuple):
        name: str
        aliases: tuple
        kwarg: bool
        values: tuple

    # TODO: Check for duplicates
    _options = {}
    _ALL_ADD_OPTION_KWARGS = {'aliases': '', 'kwarg': False, 'values': ''}
    @classmethod
    def add_option(cls, name, **kwargs):
        opt_kwargs = {
            'aliases': (cls._ALL_ADD_OPTION_KWARGS['aliases']),
            'kwarg':  cls._ALL_ADD_OPTION_KWARGS['kwarg'],
            'values': (cls._ALL_ADD_OPTION_KWARGS['values'])
        }

        # TODO: Check for duplicate keywords
        for k, v in kwargs.items():
            if k not in cls._ALL_ADD_OPTION_KWARGS:
                logging.debug('%-10s: %s', k, v)
                logging.warning("'%s' is not a valid keyword.", k)
                continue

            if (k == 'kwarg' and not isinstance(v, bool)):
                logging.warning(
                    "'kwarg' requires type 'bool', but type '%s' was given",
                    type(v).__name__)

                if 'values' in kwargs:
                    logging.info(
                        "Specified specific values for option '%s'.  %s",
                        name,
                        "Assuming 'kwarg' is to be 'True'.")

                    if not kwargs['values']:
                        logging.warning(
                            "'Values' was specified..  But none were given..")

                    opt_kwargs[k] = True
                    continue
                else:
                    logging.info("Keyword 'values' was not given.  Aassuming "
                                 + "'kwarg' is to be 'False'")
                    opt_kwargs[k] = False
                    continue
            elif k == 'kwarg':
                opt_kwargs[k] = v
                continue

            if not isinstance(v, tuple):
                v = tuple(set(v))

            opt_kwargs[k] = v

        cls._options.update({
            name.replace('-', '_'): cls._Option(name=name,
                                                aliases=opt_kwargs['aliases'],
                                                kwarg=(
                                                    opt_kwargs['kwarg']
                                                    or opt_kwargs['values']),
                                                values=opt_kwargs['values'])})

    @classmethod
    def _is_opt(cls, option):
        return (option.replace('-', '_') in cls._options
                or (any(option in opt.aliases)
                    for opt in cls._options.values()))

    @classmethod
    def _get_opt(cls, opt):
        if cls._is_opt(opt):
            for k, v in cls._options.items():
                if opt.replace('-', '_') == k or opt in v.aliases:
                    return cls._options[k]

        logging.warning("'%s' is not a valid option!", opt)
        return None

    @classmethod
    def get_option(cls, option):
        """Returns an instance of Option option

            Arguments, required:
                option: Option that is present in dict cls._options.
                    Do not include any leading dashes (-) or underscores (_).

                    Can either be the key (Name of option with '-' replaced
                    with '_'.

                    Can be the name of the option as it would be used on the
                    command line.

                    Could be an aliase (If any) of an option.

                    Can be the name or aliase (If any) of an argument (Same as
                    the option name)

                    Can be the name or aliase (If any) of a keyword (Same as
                    the option name)

            If opt is invalid, an error is thrown and script exits with error
                code 10.
        """
        option = cls._get_opt(option)
        if option:
            return option

        logging.error("'%s' is not a valid option!", option)
        sys.exit(10)

    @classmethod
    def has_arg(cls, arg):
        """Checks for argument arg

            Arguments, required:
                arg: argument that is present in dict cls._options.
                    Do not include any leading dashes (-) or underscores (_).

                    arg can only be the name of an Option (Or aliase) that is
                        not a keyword argument except for if the arg.values
                        contains 'None' in it's tuple.

            Returns True if all conditions are met, otherwise False.
        """
        tmp_opt = cls._get_opt(arg)
        return tmp_opt and (not tmp_opt.kwarg or None in tmp_opt.values)

    @classmethod
    def get_arg(cls, arg):
        """Returns an instance of the Option based on arg.

            Arguments, required:
                arg: argument that is present in dict cls._options.
                    Do no include any leading dashes (-) or underscores (_).

                    See has_arg()

            If arg is invalid, an error is thrown and script exits with error
                code 11.
        """
        tmp_opt = None if not cls.has_arg(arg) else cls._get_opt(arg)
        if tmp_opt:
            return tmp_opt

        logging.error("'%s' is not a valid argument!", arg)
        sys.exit(11)

    @classmethod
    def has_kwarg(cls, kwarg):
        """Checks for keyword argument kwarg

            Arguments, required:
                kwarg: keyword argument that is present in dict cls._options.
                    Do not include any leading dashes (-) or underscores (_).

                    kwarg can only be the name of an Option (Or aliase) that is
                        keyword argument.

            Returns True if all conditions are met, otherwise False.
        """
        tmp_opt = cls._get_opt(kwarg)
        return tmp_opt and tmp_opt.kwarg

    @classmethod
    def get_kwarg(cls, kwarg):
        """Returns an instance of the Option based on karg.

            Arguments, required:
                karg: keyword argument that is present in dict cls._options.
                    Do no include any leading dashes (-) or underscores (_).

                    See has_kwarg()

            If kwarg is invalid, an error is thrown and script exits with error
                code 12.
        """
        tmp_opt = None if not cls.has_kwarg(kwarg) else cls._get_opt(kwarg)
        if tmp_opt:
            return tmp_opt

        logging.error("'%s' is not a valid keyword argument!", kwarg)
        sys.exit(12)

    @classmethod
    def has_option(cls, option):
        """Checks for Option option

            Arguments, required:
                option: Option that is present in dict cls._options.
                    Do not include any leading dashes (-) or underscores (_).

                    Can either be the key (Name of option with '-' replaced
                    with '_'.

                    Can be the name of the option as it would be used on the
                    command line.

                    Could be an aliase (If any) of an option.

                    Can be the name or aliase (If any) of an argument (Same as
                    the option name)

                    Can be the name or aliase (If any) of a keyword (Same as
                    the option name)

            Returns True if all conditions are met, otherwise False.
        """
        return cls._is_opt(option)

    @classmethod
    def has_values(cls, kwarg):
        """Checks if kwarg has any values."""
        tmp_opt = cls._get_opt(kwarg)
        return tmp_opt and tmp_opt.values

class RepoTool(Enum):
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r head'
    HG_TOOL = 'hg clone'
    UND = 'Undetermined'

class RepoBase(ABC):

    _DIR_KW = ('srcdir', 'prefix', 'execc-prefix', 'bindir', 'sbindir',
               'libexecdir', 'sysconfdir', 'sahredstatedir', 'localstatedir',
               'libdir', 'includedir', 'oldincludedir', 'datarootdir',
               'datadir', 'localdir', 'mandir', 'docdir', 'htmldir', 'dvidir',
               'pdfdir', 'psdir', 'with-sysroot', 'with-libiconv-prefix')


    # NOTE: This isn't exactly ideal on handling if the key is
    #   'RepoTool.CURL_TOOL' or 'RepoTool.UND', but it's good enough for now.
    _REPOTOOL_TO_UPDATE_CMD = {
        RepoTool.CURL_TOOL: ["echo 'Update via \'curl\' not implemented!'"],
        RepoTool.GIT_TOOL: ['git pull'],
        RepoTool.SVN_TOOL: ['svn up'],
        RepoTool.HG_TOOL: ['hg pull', 'hg update'],
        RepoTool.UND: ["echo 'RepoTool undetermined...'"]
    }

    def __init__(self,
                 name,
                 repo_tool=RepoTool.UND,
                 repo_url='Not specified',
                 switch='Not specified'):
        super().__init__()
        self.name = name
        self.repo_tool = repo_tool
        self.repo_url = repo_url
        self.switch = switch

    @staticmethod
    def _to_abspath(path_str):
        if not os.path.isabs(path_str):
            logging.warning("'%s' is not an absolute path!", path_str)
            logging.debug("Getting absolute path for '%s'...", path_str)
            path_str = os.path.abspath(path_str)

        logging.debug('absolute path: %s', path_str)
        return path_str

    def _is_dir(self, path_str):
        path_str = self._to_abspath(path_str)
        tmp_path = Path(path_str)
        if tmp_path.is_dir():
            return True

        logging.warning("'%s' is not a directory!", tmp_path)
        return False

    @abstractmethod
    def get_config(self, *args, **kwargs):
        raise NotImplementedError("'get_config()' Not Implemented!")

    @abstractmethod
    def get_repo_download(self):
        raise NotImplementedError("'get_repo_download()' Not Implemented!")

    def get_update_commands(self):
        logging.info("Updating repository '%s' ...", self.name)
        return self._REPOTOOL_TO_UPDATE_CMD[self.repo_tool]
