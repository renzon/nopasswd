# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    babel_cfg = os.path.join(".", "babel.cfg")
    target = os.path.join("..", "src")
    msgs_pot = os.path.join(target, "locale", "messages.pot")

    os.system("pybabel extract -F %s -o %s %s" % (babel_cfg, msgs_pot, target))
    locales = ["en_US", "pt_BR"]
    locale_target=os.path.join(target,"locale")
    for loc in locales:
        os.system("pybabel update -l %s -d %s -i %s" % (loc, locale_target , msgs_pot))
    os.system("pybabel compile -f -d %s"%locale_target)


