#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pip
Version  : 21.3.1
Release  : 135
URL      : https://files.pythonhosted.org/packages/da/f6/c83229dcc3635cdeb51874184241a9508ada15d8baa337a41093fab58011/pip-21.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/da/f6/c83229dcc3635cdeb51874184241a9508ada15d8baa337a41093fab58011/pip-21.3.1.tar.gz
Summary  : The PyPA recommended tool for installing Python packages.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC LGPL-2.1 MIT Python-2.0
Requires: pypi-pip-bin = %{version}-%{release}
Requires: pypi-pip-license = %{version}-%{release}
Requires: pypi-pip-python = %{version}-%{release}
Requires: pypi-pip-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: pip
Provides: pip-python
Provides: pip-python3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
pip - The Python Package Installer
==================================
.. image:: https://img.shields.io/pypi/v/pip.svg
:target: https://pypi.org/project/pip/

%package bin
Summary: bin components for the pypi-pip package.
Group: Binaries
Requires: pypi-pip-license = %{version}-%{release}

%description bin
bin components for the pypi-pip package.


%package license
Summary: license components for the pypi-pip package.
Group: Default

%description license
license components for the pypi-pip package.


%package python
Summary: python components for the pypi-pip package.
Group: Default
Requires: pypi-pip-python3 = %{version}-%{release}

%description python
python components for the pypi-pip package.


%package python3
Summary: python3 components for the pypi-pip package.
Group: Default
Requires: python3-core
Provides: pypi(pip)

%description python3
python3 components for the pypi-pip package.


%prep
%setup -q -n pip-21.3.1
cd %{_builddir}/pip-21.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641468805
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pip
cp %{_builddir}/pip-21.3.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/f9fe0a71ce407d6b1fd2b78044794af8a1e5c47e
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/cachecontrol/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/392dcf81ae313bf981bb6e24834f3145bff49869
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/chardet/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/545f380fb332eb41236596500913ff8d582e3ead
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/colorama/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/151478b5f4a6291addb13da92ef3534597ed39a4
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/distlib/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/79c85e153df486fd6c05a2f7359e1ff6dc288867
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/distro.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/c700a8b9312d24bdc57570f7d6a131cf63d89016
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/html5lib/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/5bd527c7e2297d365b33ea67a400b6ba995e3705
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/idna/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pip/866a241848aa26cbcbfd3ca29c4a699faaee0e33
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/msgpack/COPYING %{buildroot}/usr/share/package-licenses/pypi-pip/175e59be229a5bedc6be93e958a970385bb04a62
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/packaging/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-pip/598f87f072f66e2269dd6919292b2934dbb20492
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/packaging/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-pip/fdc0e4eabc45522b079deff7d03d70528d775dc0
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/pep517/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/pkg_resources/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/a5234543d56e03c950c0080826b53a0cb97671af
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/platformdirs/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/1a628675f3f38f1d4715ebd772a8160a0ea94dd4
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/progress/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/eac6598dd7b5c07e1b517ab9ef5b242404f156b2
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/pyparsing.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/df156c6a0a89ed2a3bd4a473c68cf85907509ca0
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/requests/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/57aed0b0f74e63f6b85cce11bce29ba1710b422b
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/resolvelib/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/e8f006df7200afbbdd3a2e7a85e487338dc75073
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/six.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/ac6ba16d8833b691bbbda7c8eb0c06891c78f98f
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/tenacity/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/tomli/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/urllib3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/fae7d86a68e1724238ed64674e4cd743a7dc6796
cp %{_builddir}/pip-21.3.1/src/pip/_vendor/webencodings/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/7fc0f2700538e74dea84d45d0dd3e76f01e8103c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/pip/_vendor/distlib/t32.exe
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/pip/_vendor/distlib/w32.exe
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/pip/_vendor/distlib/w64.exe
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/pip/_vendor/distlib/t64.exe

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pip
/usr/bin/pip3
/usr/bin/pip3.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pip/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/pypi-pip/151478b5f4a6291addb13da92ef3534597ed39a4
/usr/share/package-licenses/pypi-pip/175e59be229a5bedc6be93e958a970385bb04a62
/usr/share/package-licenses/pypi-pip/1a628675f3f38f1d4715ebd772a8160a0ea94dd4
/usr/share/package-licenses/pypi-pip/392dcf81ae313bf981bb6e24834f3145bff49869
/usr/share/package-licenses/pypi-pip/545f380fb332eb41236596500913ff8d582e3ead
/usr/share/package-licenses/pypi-pip/57aed0b0f74e63f6b85cce11bce29ba1710b422b
/usr/share/package-licenses/pypi-pip/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-pip/5bd527c7e2297d365b33ea67a400b6ba995e3705
/usr/share/package-licenses/pypi-pip/79c85e153df486fd6c05a2f7359e1ff6dc288867
/usr/share/package-licenses/pypi-pip/7fc0f2700538e74dea84d45d0dd3e76f01e8103c
/usr/share/package-licenses/pypi-pip/866a241848aa26cbcbfd3ca29c4a699faaee0e33
/usr/share/package-licenses/pypi-pip/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
/usr/share/package-licenses/pypi-pip/a5234543d56e03c950c0080826b53a0cb97671af
/usr/share/package-licenses/pypi-pip/ac6ba16d8833b691bbbda7c8eb0c06891c78f98f
/usr/share/package-licenses/pypi-pip/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
/usr/share/package-licenses/pypi-pip/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/pypi-pip/df156c6a0a89ed2a3bd4a473c68cf85907509ca0
/usr/share/package-licenses/pypi-pip/e8f006df7200afbbdd3a2e7a85e487338dc75073
/usr/share/package-licenses/pypi-pip/eac6598dd7b5c07e1b517ab9ef5b242404f156b2
/usr/share/package-licenses/pypi-pip/f9fe0a71ce407d6b1fd2b78044794af8a1e5c47e
/usr/share/package-licenses/pypi-pip/fae7d86a68e1724238ed64674e4cd743a7dc6796
/usr/share/package-licenses/pypi-pip/fdc0e4eabc45522b079deff7d03d70528d775dc0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
