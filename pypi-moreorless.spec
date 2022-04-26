#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-moreorless
Version  : 0.4.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/c5/5d/c8ed33403f62a2f755905c8d2d36b71e3fc32588deeb53ad1206edbb067a/moreorless-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/5d/c8ed33403f62a2f755905c8d2d36b71e3fc32588deeb53ad1206edbb067a/moreorless-0.4.0.tar.gz
Summary  : Python diff wrapper
Group    : Development/Tools
License  : MIT
Requires: pypi-moreorless-license = %{version}-%{release}
Requires: pypi-moreorless-python = %{version}-%{release}
Requires: pypi-moreorless-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)

%description
This is a thin wrapper around `difflib.unified_diff` that Does The Right Thing

%package license
Summary: license components for the pypi-moreorless package.
Group: Default

%description license
license components for the pypi-moreorless package.


%package python
Summary: python components for the pypi-moreorless package.
Group: Default
Requires: pypi-moreorless-python3 = %{version}-%{release}

%description python
python components for the pypi-moreorless package.


%package python3
Summary: python3 components for the pypi-moreorless package.
Group: Default
Requires: python3-core
Provides: pypi(moreorless)
Requires: pypi(click)

%description python3
python3 components for the pypi-moreorless package.


%prep
%setup -q -n moreorless-0.4.0
cd %{_builddir}/moreorless-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651015512
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-moreorless
cp %{_builddir}/moreorless-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-moreorless/4ac95a2647251996cf4946651f3f7afa3f8d7369
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-moreorless/4ac95a2647251996cf4946651f3f7afa3f8d7369

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
