#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : pypi-pip
Version  : 25.0.1
Release  : 184
URL      : https://files.pythonhosted.org/packages/70/53/b309b4a497b09655cb7e07088966881a57d082f48ac3cb54ea729fd2c6cf/pip-25.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/70/53/b309b4a497b09655cb7e07088966881a57d082f48ac3cb54ea729fd2c6cf/pip-25.0.1.tar.gz
Summary  : The PyPA recommended tool for installing Python packages.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0 Python-2.0
Requires: pypi-pip-bin = %{version}-%{release}
Requires: pypi-pip-license = %{version}-%{release}
Requires: pypi-pip-python = %{version}-%{release}
Requires: pypi-pip-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
pip - The Python Package Installer
==================================
.. |pypi-version| image:: https://img.shields.io/pypi/v/pip.svg
:target: https://pypi.org/project/pip/
:alt: PyPI

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
%setup -q -n pip-25.0.1
cd %{_builddir}/pip-25.0.1
pushd ..
cp -a pip-25.0.1 buildavx2
popd
pushd ..
cp -a pip-25.0.1 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740084366
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd
pushd ../buildapx/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pip
cp %{_builddir}/pip-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/d1816736d55c943e1ed44a003f72cb7d1afe0789 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/cachecontrol/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/29bee62daa11fe00707573e32779de8b2dc12cb5 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/certifi/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/3b4d48f29780c79b4484b1b3979544766b626fdb || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/distlib/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/79c85e153df486fd6c05a2f7359e1ff6dc288867 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/distro/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/c700a8b9312d24bdc57570f7d6a131cf63d89016 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/idna/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pip/97e2c8c10633ca4a49876343c652e92e7515c36f || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/msgpack/COPYING %{buildroot}/usr/share/package-licenses/pypi-pip/175e59be229a5bedc6be93e958a970385bb04a62 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/packaging/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-pip/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/packaging/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-pip/fdc0e4eabc45522b079deff7d03d70528d775dc0 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/pkg_resources/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/0445ed0f69910eeaee036f09a39a13c6e1f37e12 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/platformdirs/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/f511a8a63af8c6e36004b593478436bbc560ee0c || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/pygments/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/0c271aeb0199762f47e124c8960b830ad5a97ce0 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/pyproject_hooks/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/requests/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/57aed0b0f74e63f6b85cce11bce29ba1710b422b || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/resolvelib/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/e8f006df7200afbbdd3a2e7a85e487338dc75073 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/rich/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/tomli/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/truststore/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/8700b70e60a895a86d72b16eb1214ef9c51e5cb9 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/typing_extensions.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pip/c6e195f9aa30cc9b675d1612ca4fb7f74111bd35 || :
cp %{_builddir}/pip-%{version}/src/pip/_vendor/urllib3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pip/fae7d86a68e1724238ed64674e4cd743a7dc6796 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
pushd ../buildapx/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-va dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.13/site-packages/pip/_vendor/distlib/t32.exe
rm -f %{buildroot}*/usr/lib/python3.13/site-packages/pip/_vendor/distlib/t64-arm.exe
rm -f %{buildroot}*/usr/lib/python3.13/site-packages/pip/_vendor/distlib/t64.exe
rm -f %{buildroot}*/usr/lib/python3.13/site-packages/pip/_vendor/distlib/w32.exe
rm -f %{buildroot}*/usr/lib/python3.13/site-packages/pip/_vendor/distlib/w64-arm.exe
rm -f %{buildroot}*/usr/lib/python3.13/site-packages/pip/_vendor/distlib/w64.exe
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pip
/usr/bin/pip3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pip/0445ed0f69910eeaee036f09a39a13c6e1f37e12
/usr/share/package-licenses/pypi-pip/0c271aeb0199762f47e124c8960b830ad5a97ce0
/usr/share/package-licenses/pypi-pip/175e59be229a5bedc6be93e958a970385bb04a62
/usr/share/package-licenses/pypi-pip/29bee62daa11fe00707573e32779de8b2dc12cb5
/usr/share/package-licenses/pypi-pip/3b4d48f29780c79b4484b1b3979544766b626fdb
/usr/share/package-licenses/pypi-pip/57aed0b0f74e63f6b85cce11bce29ba1710b422b
/usr/share/package-licenses/pypi-pip/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-pip/79c85e153df486fd6c05a2f7359e1ff6dc288867
/usr/share/package-licenses/pypi-pip/8700b70e60a895a86d72b16eb1214ef9c51e5cb9
/usr/share/package-licenses/pypi-pip/97e2c8c10633ca4a49876343c652e92e7515c36f
/usr/share/package-licenses/pypi-pip/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
/usr/share/package-licenses/pypi-pip/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2
/usr/share/package-licenses/pypi-pip/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
/usr/share/package-licenses/pypi-pip/c6e195f9aa30cc9b675d1612ca4fb7f74111bd35
/usr/share/package-licenses/pypi-pip/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/pypi-pip/d1816736d55c943e1ed44a003f72cb7d1afe0789
/usr/share/package-licenses/pypi-pip/e8f006df7200afbbdd3a2e7a85e487338dc75073
/usr/share/package-licenses/pypi-pip/f511a8a63af8c6e36004b593478436bbc560ee0c
/usr/share/package-licenses/pypi-pip/fae7d86a68e1724238ed64674e4cd743a7dc6796
/usr/share/package-licenses/pypi-pip/fdc0e4eabc45522b079deff7d03d70528d775dc0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
