==========
AttachTags
==========


.. image:: https://img.shields.io/pypi/v/attachtags.svg
        :target: https://pypi.python.org/pypi/attachtags

.. image:: https://img.shields.io/travis/Gongzi-Yu/attachtags.svg
        :target: https://travis-ci.com/Gongzi-Yu/attachtags

.. image:: https://readthedocs.org/projects/attachtags/badge/?version=latest
        :target: https://attachtags.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

attachtags is a tool for recording and categorizing files in your Windows. Use it to help you organize and categorize files that are difficult to remember.

.. _header-n3:

Introduction
-------------

Have we all had this idea, wanting to figure out what files are in our computer? But various file formats and messy file names always give us headaches. After figuring out what these files were doing in various ways, a few days later, I forgot it again.

Or this situation: when we delete a software, there will always be some unknown files left in the computer. I want to clean the computer and delete useless files, but I don't know which are important files and which can be deleted.

attachtags is a command line script tool made to solve this problem. By adding a memorable label to a file or folder, the purpose of recording and classifying files is achieved.

* Free software: MIT license
* Documentation: https://attachtags.readthedocs.io.

.. _header-n6:

attachtags commands
--------------------

.. code::

   usage: attachtags [-h] [-v] [-l]
                     {create,delete,rename,show,search,attach,remove} ...

   positional arguments:
     {create,delete,rename,show,search,attach,remove}
       create              create one new tag
       delete              delete one tag
       rename              rename some tags with a new name
       show                show tags from some path
       search              search paths with this tags in this path
       attach              attach a tag to some paths
       remove              remove a tag from some paths

   optional arguments:
     -h, --help            show this help message and exit
     -v, --version         show program's version number and exit
     -l, --list            list all tags

.. _header-n8:

Installation
------------

First, you must have python (version>=3.7) in your computer!

.. _header-n10:

With ``pip``
~~~~~~~~~~~~~

.. code::

   pip install attachtags

.. _header-n12:

Usage
-----

.. _header-n13:

``-h`` , ``-v`` , ``-l``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``-h`` is used to display help documents, you can use ``-h`` for all ``{create,delete,rename,show,search,attach,remove}`` to display the corresponding help documents;
``-v`` is used to display the current script of the script, ``-l`` is used to display the existing tags

.. _header-n16:

``create`` , ``delete`` , ``rename``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``create`` is used to create one or more new tags

``delete`` is used to delete one or more tags

``rename`` is used to rename one or more tags

.. _header-n20:

``attach`` , ``remove``
~~~~~~~~~~~~~~~~~~~~~~~~~~

``attach`` is used to attach a tag to a file or folder, using ``--all-in-dirs`` can attach a tag to all files and folders in a folder;

``remove`` is used to remove a tag from a file or folder. Use ``--all-in-dirs`` to remove a tag from all files and folders in a folder;

.. _header-n23:

``show`` , ``search``
~~~~~~~~~~~~~~~~~~~~~~~~

``show`` can show the tags attached to a file or folder, and use ``-s`` to show multiple tags;

``search`` can search for files or folders in a folder if they have the tag you entered, and output them;

.. _header-n26:

How to update attachtags
------------------------

.. code::

   pip install --upgrade attachtags

.. _header-n28:

Bug Tracker and Support
-----------------------

Please report any suggestions, bug reports, or annoyances with attachtags through the `GitHub
bug
tracker <https://github.com/Gongzi-Yu/attachtags/issues>`__.

.. _header-n30:

Author
------

attachtags was developed by
`Gongzi-Yu (Gongzi-Yu) (github.com) <https://github.com/Gongzi-Yu>`__.
Thanks for all Contributors and Supports for patience for the latest major release.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
