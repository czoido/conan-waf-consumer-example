import os
from shutil import copy

from conans import ConanFile, tools, python_requires

base = python_requires("waf-build-helper/0.1@czoido/testing")


class TestWafConan(base.get_conanfile()):
    settings = "os", "compiler", "build_type", "arch", "arch_build"
    generators = "Waf"
    requires = "mylib-waf/1.0@czoido/testing"
    build_requires = "WafGen/0.1@czoido/testing", "waf/2.0.17@czoido/testing"
    exports_sources = "wscript", "main.cpp"

    def build(self):
        waf = base.WafBuildEnvironment(self)
        waf.configure()
        waf.build()
